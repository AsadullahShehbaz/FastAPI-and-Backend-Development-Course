from httpx import AsyncClient
from app.tests import example
from app.tests.conftest import test_id

# @pytest.mark.asyncio
async def test_app(client: AsyncClient) -> None:
    print("Testing App endpoint...")
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json()["detail"] == str(test_id)

from httpx import AsyncClient


async def test_seller_login(client: AsyncClient) -> None:
    response = await client.post(
        "/seller/login",
        data={
            "username": example.SELLER["email"],
            "password": example.SELLER["password"],
            "grant_type": "password",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

async def test_submit_product_requires_authentication(client: AsyncClient) -> None:
    response = await client.post(
        "/product/v1/",
        json={},
    )

    assert response.status_code == 401


async def test_seller_can_submit_product(
    client: AsyncClient,
    seller_token: str,
) -> None:
    response = await client.post(
        "/product/v1/",
        json=example.PRODUCT,
        headers={"Authorization": f"Bearer {seller_token}"},
    )

    assert response.status_code == 201
    product_id = response.json()["id"]

    get_response = await client.get(
        "/product/v1/",
        params={"id": product_id},
        headers={"Authorization": f"Bearer {seller_token}"},
    )

    assert get_response.status_code == 200

