#!/usr/bin/python3
import asyncio
import random

async def api_call(attempt):
    if random.random() < 0.7:
        raise Exception("Temporary Failure")
    return f"attempt {attempt} Succeded"

async def jitter(func, max_attempt=5, base_delay=1):
    for attempt in range(max_attempt):
        try:
            result = await func(attempt)
            print(f"Attempt {attempt + 1}: {result}")
            return result
        except Exception as e:
            if attempt == max_attempt - 1:
                print(f"Failed after max attempt")
                raise
            delay = random.uniform(0, base_delay * (2 ** attempt))
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f} seconds...")
            await asyncio.sleep(delay)

async def main():
    await jitter(api_call)

if __name__ == "__main__":
    asyncio.run(main())