#!/usr/bin/python3
import time


class LeakingBucket:
    def __init__(self, bucket_size, leak_rate):
        self.bucket_size = bucket_size
        self.leak_rate = leak_rate
        self.current_level = 0
        self.last_time = time.time()
    
    def _leak(self):
        current_time = time.time()
        time_diff = current_time - self.last_time
        leaked_amount = time_diff * self.leak_rate
        self.current_level = max(0, self.current_level - leaked_amount)
        self.last_time = current_time
    
    def allow(self, amount=1):
        self._leak()
        if self.current_level + amount <= self.bucket_size:
            self.current_level += amount
            return True
        return False


if __name__ == "__main__":
    bucket = LeakingBucket(bucket_size=5, leak_rate=1)

    for i in range(30):
        if bucket.allow():
            print(f"Request {i + 1} passed")
        else:
            print(f"Request {i + 1} failed and is not allowed")
        time.sleep(0.1)