# Lecture 3.2 (part 2) - How a decorator can do ROUTING
# (This is NOT how FastAPI works internally - it only shows the idea.)
from typing import Any, Callable

routes: dict[str, Callable[..., Any]] = {}


def route(path: str):
    def register_route(func):
        routes[path] = func      # remember: path -> function
        return func              # give the function back unchanged
    return register_route


@route("/product")
def get_product():
    return "Product<1001, Wireless Mouse, 18.99>"


request: str = ""

while request != "quit":
    request = input(">   ")

    if request in routes:
        print(routes[request](), end="\n\n")
    elif request != "quit":
        print("Not found")
