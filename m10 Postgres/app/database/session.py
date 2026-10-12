from datetime import datetime, timedelta, timezone

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel, select

from app.config import settings
from app.database.models import Product, ProductStatus

# ASYNC engine; no SQLite-only connect_args any more
engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True,
)

# Session factory (pooling, thread safety). expire_on_commit=False keeps
# objects usable after commit() so refresh()/return still work.
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_db_tables():
    async with engine.begin() as connection:
        from app.database.models import Product  # noqa: F401  (register model)
        # create_all is SYNC, so run it through run_sync (pass it, don't call it)
        await connection.run_sync(SQLModel.metadata.create_all)


async def seed_products():
    """Bonus: load the 7 starter products when the table is empty."""
    starter = [
        ("Wireless Mouse", 18.99, 42, 1), ("Mechanical Keyboard", 64.99, 18, 2),
        ("USB-C Hub", 29.99, 35, 1), ("Laptop Stand", 39.99, 12, 3),
        ("Webcam", 54.99, 25, 2), ("Bluetooth Speaker", 44.99, 30, 4),
        ("External SSD", 89.99, 10, 5),
    ]
    async with async_session() as session:
        result = await session.execute(select(Product.id).limit(1))
        if result.first() is None:
            for name, price, stock, warehouse in starter:
                session.add(Product(
                    name=name, price=price, stock=stock, warehouse=warehouse,
                    status=ProductStatus.low_stock if stock <= 12 else ProductStatus.active,
                    warranty_until=datetime.now(timezone.utc) + timedelta(days=365),
                ))
            await session.commit()


# Async generator dependency: one session per request
async def get_session():
    async with async_session() as session:
        yield session
