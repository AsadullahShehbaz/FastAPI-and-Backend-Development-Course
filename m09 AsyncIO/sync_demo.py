# Lecture 9.1 - The problem: synchronous request handling
import time


def endpoint(route: str) -> str:
    print(f">> handling {route}")

    # emulate a slow database call (real ones take 10-300 ms; we use 1 s)
    time.sleep(1)

    print(f"<< response {route}")
    return route


def server():
    tests = (
        "GET /product?id=1001",
        "PATCH /product?id=1004",
        "GET /product?id=1003",
    )

    start = time.perf_counter()

    for route in tests:          # one after another...
        endpoint(route)

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds")     # ~3.00


server()
