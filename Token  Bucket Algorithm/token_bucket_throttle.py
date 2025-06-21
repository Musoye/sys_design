#!/usr/bin/python3
import asyncio
import time


class AsyncTokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.tokens = capacity
        self.last_time = time.time()
        self.lock = asyncio.Lock()  # to prevent race conditions

    def _refill(self):
        current_time = time.time()
        time_diff = current_time - self.last_time
        added_tokens = time_diff * self.fill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_time = current_time

    async def allow(self, tokens_required=1):
        async with self.lock:
            while True:
                self._refill()
                if self.tokens >= tokens_required:
                    self.tokens -= tokens_required
                    return True
                await asyncio.sleep(0.1)


async def simulate_request(bucket, request_id):
    await bucket.allow()
    print(f"Request {request_id} processed at {time.strftime('%X')}")


async def main():
    bucket = AsyncTokenBucket(capacity=5, fill_rate=1)

    tasks = []
    for i in range(20):
        task = asyncio.create_task(simulate_request(bucket, i + 1))
        await asyncio.sleep(0.1)
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
