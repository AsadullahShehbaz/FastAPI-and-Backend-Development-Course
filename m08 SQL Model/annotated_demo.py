# Lecture 8.4 (part 2) - typing.Annotated: attach metadata to a type
from typing import Annotated

# A plain hint says "float" but not WHICH currency
price: Annotated[float, "USD"] = 18.99

# Store it once, reuse everywhere
USD = Annotated[float, "USD"]
laptop_stand_price: USD = 39.99

print(USD.__origin__)         # <class 'float'>
print(USD.__metadata__)       # ('USD',)
print(USD.__metadata__[0])    # USD
