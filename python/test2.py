import time
import asyncio


async def timerX():
    for i in range(5):
        print(f'Iteration: {i + 1}')
        await asyncio.sleep(1)  # time.sleep(1)


async def countX():
    for i in range(5):
        print(f'Iteration2: {i + 1}')
        await asyncio.sleep(1)  # time.sleep(1)


async def main():
    await asyncio.gather(timerX(), countX())


asyncio.run(main())
