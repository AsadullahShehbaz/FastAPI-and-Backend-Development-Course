# Lecture 9.3 - Run coroutines CONCURRENTLY: create_task + wait  (~1 second)
import asyncio
import time


async def endpoint(route: str) -> str:
    print(f">> handling {route}")
    await asyncio.sleep(1)                 # emulate database delay
    print(f"<< response {route}")
    return route


async def server():
    tests = (
        "GET /product?id=1001",
        "PATCH /product?id=1004",
        "GET /product?id=1003",
    )

    start = time.perf_counter()

    # 1) wrap every coroutine in a task -> they start running together
    requests = [
        asyncio.create_task(endpoint(route))
        for route in tests
    ]

    # 2) wait is a FUNCTION returning a coroutine -> await it
    finished, pending = await asyncio.wait(requests)

    # 3) read each return value (finished is a set -> order not guaranteed)
    for task in finished:
        print("Result:", task.result())

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds")     # ~1.00


asyncio.run(server())
