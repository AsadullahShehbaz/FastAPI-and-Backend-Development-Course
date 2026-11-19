from uuid import UUID

import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.database.models import Tag, TagName
from app.main import app
from app.tests import example
from app.tests.conftest import TestSession
from app.utils import generate_url_safe_token


@pytest_asyncio.fixture
async def product(
    client: AsyncClient,
    seller_token: str,
) -> dict:
    response = await client.post(
        "/product/v1/",
        json=example.PRODUCT,
        headers={"Authorization": f"Bearer {seller_token}"},
    )
    assert response.status_code == 201

    product_data = response.json()
    yield product_data

    if product_data["status"] != "cancelled":
        current = await client.get(
            f"/product/v1/{product_data['id']}",
        )
        if current.status_code == 200 and current.json()["status"] != "cancelled":
            await client.get(
                "/product/v1/",
                params={"id": product_data["id"]},
                headers={"Authorization": f"Bearer {seller_token}"},
            )


async def test_product_openapi_contract() -> None:
    schema = app.openapi()
    expected_operations = {
        "/product/v1/tag": {"post", "delete"},
        "/product/v1/tagged": {"get"},
        "/product/v1/review": {"get", "post"},
        "/product/v1/{id}": {"get"},
        "/product/v1/": {"get", "post", "patch"},
    }

    for path, methods in expected_operations.items():
        assert methods <= schema["paths"][path].keys()

    product_create = schema["components"]["schemas"]["ProductCreate"]
    assert product_create["required"] == [
        "name",
        "price",
        "stock",
        "destination",
        "client_contact_email",
    ]
    assert product_create["properties"]["name"]["minLength"] == 3
    assert product_create["properties"]["price"]["exclusiveMinimum"] == 0.0
    assert product_create["properties"]["stock"]["exclusiveMinimum"] == 0.0


async def test_create_product_rejects_invalid_openapi_fields(
    client: AsyncClient,
    seller_token: str,
) -> None:
    invalid_product = {
        **example.PRODUCT,
        "name": "AB",
        "price": 0,
        "stock": 0,
        "client_contact_email": "not-an-email",
    }

    response = await client.post(
        "/product/v1/",
        json=invalid_product,
        headers={"Authorization": f"Bearer {seller_token}"},
    )

    assert response.status_code == 422


async def test_create_product_rejects_unserviceable_destination(
    client: AsyncClient,
    seller_token: str,
) -> None:
    response = await client.post(
        "/product/v1/",
        json={**example.PRODUCT, "destination": 99999},
        headers={"Authorization": f"Bearer {seller_token}"},
    )

    assert response.status_code == 406


async def test_get_product_by_path_id(
    client: AsyncClient,
    product: dict,
) -> None:
    response = await client.get(f"/product/v1/{product['id']}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == product["id"]
    assert body["status"] == "placed"
    assert body["name"] == example.PRODUCT["name"]
    assert body["seller"]["email"] == example.SELLER["email"]
    assert body["timeline"]
    assert body["tags"] == []


async def test_get_product_rejects_invalid_path_uuid(client: AsyncClient) -> None:
    response = await client.get("/product/v1/not-a-uuid")

    assert response.status_code == 422


async def test_get_missing_product_returns_not_found(client: AsyncClient) -> None:
    response = await client.get(
        "/product/v1/87654321-4321-8765-4321-876543218765"
    )

    assert response.status_code == 404


async def test_partner_can_update_product(
    client: AsyncClient,
    product: dict,
) -> None:
    login_response = await client.post(
        "/partner/login",
        data={
            "username": example.DELIVERY_PARTNER["email"],
            "password": example.DELIVERY_PARTNER["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    partner_token = login_response.json()["access_token"]

    response = await client.patch(
        "/product/v1/",
        params={"id": product["id"]},
        json={
            "status": "in_transit",
            "location": example.DELIVERY_PARTNER["zip_code"],
            "description": "On the way",
        },
        headers={"Authorization": f"Bearer {partner_token}"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "in_transit"


async def test_patch_product_requires_an_update(
    client: AsyncClient,
    product: dict,
) -> None:
    login_response = await client.post(
        "/partner/login",
        data={
            "username": example.DELIVERY_PARTNER["email"],
            "password": example.DELIVERY_PARTNER["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200

    response = await client.patch(
        "/product/v1/",
        params={"id": product["id"]},
        json={},
        headers={
            "Authorization": f"Bearer {login_response.json()['access_token']}"
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "No data provided to update"


async def test_seller_can_cancel_product(
    client: AsyncClient,
    product: dict,
    seller_token: str,
) -> None:
    response = await client.get(
        "/product/v1/",
        params={"id": product["id"]},
        headers={"Authorization": f"Bearer {seller_token}"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "cancelled"


async def test_cancelling_product_twice_returns_bad_request(
    client: AsyncClient,
    product: dict,
    seller_token: str,
) -> None:
    headers = {"Authorization": f"Bearer {seller_token}"}
    params = {"id": product["id"]}

    first_response = await client.get("/product/v1/", params=params, headers=headers)
    assert first_response.status_code == 200

    response = await client.get("/product/v1/", params=params, headers=headers)

    assert response.status_code == 400
    assert response.json()["detail"] == "Product is already cancelled"


async def test_add_and_remove_product_tag(
    client: AsyncClient,
    product: dict,
) -> None:
    async with TestSession() as session:
        session.add(
            Tag(
                name=TagName.FRAGILE,
                instruction="Handle with care",
            )
        )
        await session.commit()

    params = {"id": product["id"], "tag_name": TagName.FRAGILE.value}
    add_response = await client.post("/product/v1/tag", params=params)

    assert add_response.status_code == 200
    assert add_response.json()["tags"] == [
        {"name": TagName.FRAGILE.value, "instruction": "Handle with care"}
    ]

    tagged_response = await client.get(
        "/product/v1/tagged",
        params={"tag_name": TagName.FRAGILE.value},
    )
    assert tagged_response.status_code == 200
    assert [item["id"] for item in tagged_response.json()] == [product["id"]]

    remove_response = await client.delete("/product/v1/tag", params=params)

    assert remove_response.status_code == 200
    assert remove_response.json()["tags"] == []


async def test_add_tag_rejects_invalid_tag_enum(
    client: AsyncClient,
    product: dict,
) -> None:
    response = await client.post(
        "/product/v1/tag",
        params={"id": product["id"], "tag_name": "not-a-tag"},
    )

    assert response.status_code == 422


async def test_submit_review_accepts_openapi_rating_range(
    client: AsyncClient,
    product: dict,
) -> None:
    token = generate_url_safe_token({"id": product["id"]})

    response = await client.post(
        "/product/v1/review",
        params={"token": token},
        data={"rating": 5, "comment": "Great product"},
    )

    assert response.status_code == 200
    assert response.json() == {"detail": "Review Submitted"}


@pytest.mark.parametrize("rating", ["0", "6"])
async def test_submit_review_rejects_rating_outside_openapi_range(
    client: AsyncClient,
    rating: str,
) -> None:
    response = await client.post(
        "/product/v1/review",
        params={"token": "unused"},
        data={"rating": rating},
    )

    assert response.status_code == 422


async def test_submit_review_rejects_invalid_token(client: AsyncClient) -> None:
    response = await client.post(
        "/product/v1/review",
        params={"token": "invalid"},
        data={"rating": 3},
    )

    assert response.status_code == 401


async def test_get_review_form_returns_html(
    client: AsyncClient,
    product: dict,
) -> None:
    token = generate_url_safe_token({"id": product["id"]})

    response = await client.get(
        "/product/v1/review",
        params={"token": token},
    )

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
