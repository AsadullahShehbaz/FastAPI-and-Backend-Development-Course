from httpx import ASGITransport, AsyncClient
from uuid import UUID
import pytest_asyncio
from app.tests import example
from app.tests.example import create_test_data
from sqlmodel import SQLModel
from app.main import app,get_id
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from app.database.session import get_session

test_id = UUID("12345678-1234-5678-1234-567812345678")

def get_id_override() -> UUID:
    return test_id

@pytest_asyncio.fixture(scope="session")
async def client():
    async with AsyncClient(
        transport = ASGITransport(app=app),
        base_url="http://test"
    ) as test_client:
        yield test_client

test_engine = create_async_engine("sqlite+aiosqlite:///:memory:")
TestSession = async_sessionmaker(bind=test_engine,class_=AsyncSession,expire_on_commit=False)

async def get_session_override():
    async with TestSession() as session:
        yield session



@pytest_asyncio.fixture(scope="session",autouse=True)
async def setup_and_teardown():
    print("\nTesting Starting...")
    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[get_id] = get_id_override

    print("\nCreating Tables...")
    async with test_engine.begin() as connection:
        from app.database.models import Product,Seller,DeliveryPartner,ProductEvent,Location
        await connection.run_sync(SQLModel.metadata.create_all) 

    async with TestSession() as session:
        await create_test_data(session)
    yield 

    async with test_engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.drop_all) 

    app.dependency_overrides.clear()
    print("\nTables dropped and dependency override cleared...")

import pytest_asyncio
from httpx import AsyncClient
from app.tests import example


@pytest_asyncio.fixture(scope="session")
async def seller_token(client: AsyncClient) -> str:
    response = await client.post(
        "/seller/login",
        data={
            "username": example.SELLER["email"],
            "password": example.SELLER["password"],
            "grant_type": "password",
        },
    )

    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data

    return token_data["access_token"]
