# Lecture 6.2 - Field(): extra validation, defaults, default_factory, descriptions
import random

from pydantic import BaseModel, Field


def random_warehouse() -> int:
    return random.randint(1, 5)


class Product(BaseModel):
    name: str = Field(
        description="Product title",
        min_length=3,            # at least 3 characters
        max_length=100,          # at most 100 characters
    )
    price: float = Field(
        description="Price in US dollars",
        gt=0,                    # [g]reater [t]han 0
        le=10_000,               # [l]ess than or [e]qual to 10 000
    )
    stock: int = Field(
        description="Units available in the warehouse",
        ge=0,                    # [g]reater than or [e]qual to 0
    )
    warehouse: int | None = Field(
        description="Warehouse code (1-5). Random if not provided.",
        # default=1,             # fixed default - evaluated ONCE
        default_factory=random_warehouse,   # function REFERENCE - runs per object
    )
