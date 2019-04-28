import asyncio
import time


async def hungry():
    print("getting food")
    before = time.time()
    await asyncio.sleep(0.1)
    duration = time.time() - before
    print(f"full now, took {duration:.1f}s")


asyncio.run(hungry())


async def nap():
    print("nap time")
    time.sleep(2)
    print("nap over")


async def main():
    await asyncio.gather(hungry(), nap())


asyncio.run(main())


async def nap2():
    loop = asyncio.get_running_loop()
    print("nap time")
    await loop.run_in_executor(None, time.sleep, 2)
    print("nap over")


async def main():
    await asyncio.gather(hungry(), nap2())


asyncio.run(main())
