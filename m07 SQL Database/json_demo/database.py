# Lecture 7.1 - Persisting data in a JSON file
import json
from pathlib import Path

# JSON file next to this module (works no matter where you start the server)
FILE = Path(__file__).with_name("products.json")

products = {}


### Load: list in the file  ->  dict {id: product} in memory
with open(FILE) as json_file:
    data = json.load(json_file)            # a list of dicts

    for value in data:
        products[value["id"]] = value      # id becomes the key


### Save: dict in memory  ->  list in the file
def save():
    with open(FILE, "w") as json_file:     # "w" = write mode
        json.dump(list(products.values()), json_file, indent=2)
