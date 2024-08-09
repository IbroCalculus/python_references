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


async def timerX():
    for i in range(5):
        print(f'Iteration: {i + 1}')
        time.sleep(1)


async def countX():
    await timerX()
    print('Count completed')


asyncio.run(countX())

print("===================== THESE BELOW WILL RUN CONCURRENTLY ==========================")


async def timerX():
    for i in range(5):
        print(f'Iteration: {i + 1}')
        await asyncio.sleep(1)  # time.sleep(1) Will not work, it is a blocking call, it blocks the entire thread, preventing other threads from running concurrently


async def countX():
    for i in range(5):
        print(f'Iteration2: {i + 1}')
        await asyncio.sleep(1)  # time.sleep(1)


async def main():
    await asyncio.gather(timerX(), countX())


asyncio.run(main())
