#!/usr/bin/python3
import time

class TokenBucketAlgorithm:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity          # Maximum tokens the bucket can hold
        self.fill_rate = fill_rate        # Tokens added per second
        self.tokens = capacity            # Current tokens in the bucket
        self.last_time = time.time()      # Last time the bucket was refilled

    def _refill(self):
        current_time = time.time()
        time_diff = current_time - self.last_time
        added_tokens = time_diff * self.fill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_time = current_time 
    
    def allow(self, tokens_required=1):
        self._refill()
        if self.tokens >= tokens_required:
            self.tokens -= tokens_required
            return True
        return False

if __name__ == "__main__":
    bucket = TokenBucketAlgorithm(capacity=5, fill_rate=1)

    for i in range(30):
        if bucket.allow():
            print(f"Request {i + 1} passed")
        else:
            print(f"Request {i + 1} failed and is not allowed")
        time.sleep(0.1)
