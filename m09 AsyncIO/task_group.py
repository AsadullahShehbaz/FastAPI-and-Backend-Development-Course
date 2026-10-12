# Lecture 9.4 - asyncio.TaskGroup: the modern way (Python 3.11+)
import asyncio
import time


async def endpoint(route: str) -> str:
    print(f">> handling {route}")
    await asyncio.sleep(1)
    print(f"<< response {route}")
    return route


async def server():
    tests = (
        "GET /product?id=1001",
        "PATCH /product?id=1004",
        "GET /product?id=1003",
    )

    start = time.perf_counter()

    # "async with" because TaskGroup is an ASYNC context manager
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(endpoint(route))      # starts running immediately
            for route in tests
        ]
    # leaving the block = every task is finished

    print("Task[0] result:", tasks[0].result())  # or: await tasks[0]

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds")     # ~1.00


asyncio.run(server())
