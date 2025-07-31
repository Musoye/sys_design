#!/usr/bin/python3
import time


class FixedWindowCounter:
    def __init__(self, window_size):
        self.window_size = window_size  # Size of the time window in seconds
        self.request_count = 0          
        self.start_time = None         

    def _reset_window(self):
        if self.start_time is None or (time.time() - self.start_time) >= self.window_size:
            self.start_time = time.time()
            self.request_count = 0

    def allow(self):
        self._reset_window()
        if self.request_count < 1:
            self.request_count += 1
            return True
        return False