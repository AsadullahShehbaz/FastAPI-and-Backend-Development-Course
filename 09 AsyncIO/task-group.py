# Run Coroutines Concurrently using asyncio.create_tasks() and asyncio.wait()

import asyncio
import time
async def endpoint(route: str) -> str:
    print(f">> handling {route}")
    # emulate a slow database call (real ones take 10-300 ms; we use 1 s)
    await asyncio.sleep(1)
    # print(f"Result : {result}")
    print(f"<< response {route}")
    return route
async def server():
    tests = (
    "GET /product?id=1001",
    "PATCH /product?id=1004",
    "GET /product?id=1003",
    )
    start = time.perf_counter()


    async with asyncio.TaskGroup() as tg:
        # 1.Create Task of each coroutine 
        tasks = [tg.create_task(endpoint(test)) for test in tests]
        print(tasks[0].result())
    # for route in tests:          
    #     await endpoint(route)
    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds")     

asyncio.run(server())
