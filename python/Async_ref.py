import asyncio
import time

'''
CONSISTS OF:
    - Async/Await
    - Coroutines
    - Futures and Tasks
    - AsyncIO

async: This keyword is used to declare a function as a “coroutine.”  
       A coroutine is a special kind of function that can be paused and resumed, allowing Python to handle other tasks in the meantime. 
       It allows you to perform asynchronous operations within the function.
await: The await keyword is used inside an async function to call another async function and wait for it to finish. The function being called with await is also a coroutine

'''


async def say_hello():
    print('Hello, World!')
    await asyncio.sleep(2)
    await loopThrough()
    for i in range(5):
        print(f"Hello {i}")
        await asyncio.sleep(1)


async def loopThrough():
    for i in range(5):
        print(f"Iteration number {i}")
        await asyncio.sleep(1)

asyncio.run(say_hello())



print("===================== THESE BELOW WILL RUN CONCURRENTLY ==========================")

async def task1():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Task 1 - Iteration {i + 1}")


async def task2():
    for i in range(10):
        await asyncio.sleep(1)
        print(f"Task 2 - Iteration {i + 1}")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
