# Lecture 3.1 - Type hints (run with plain python, check with mypy)
from typing import Any


# Custom class used as a type
class Warehouse:
    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code


# Variable hints
name: str = "Wireless Mouse"
price: float = 18.99
stock: int = 42
in_stock: bool = True
barcode: bytes = b"\x00\x01"

# Two possible types -> pipe operator
discount: int | float = 10

# Optional value
note: str | None = None

# list: container + element type
product_ids: list[int] = [1001, 1002, 1003]

# tuple: fixed length, hint every position
product_row: tuple[int, str] = (1001, "Wireless Mouse")
# tuple of unknown length -> ellipsis
prices: tuple[float, ...] = (18.99, 64.99, 29.99)
# tuple with a custom class
main_store = Warehouse("Lahore Main", 1)
stored: tuple[Warehouse, int] = (main_store, 42)

# dict: key type, value type  (Any when values differ)
product: dict[str, Any] = {
    "id": 1001,
    "name": "Wireless Mouse",
    "price": 18.99,
    "stock": 42,
}


# Hinting function arguments and the return type
def apply_discount(price: float, percent: float | None = 10) -> float:
    percent = 10 if percent is None else percent
    return round(price - price * percent / 100, 2)


print(apply_discount(64.99))        # 58.49
print(apply_discount(64.99, 25))    # 48.74
