import time
from functools import wraps


class RateLimiter:
    def __init__(self, min_interval):
        self.min_interval = min_interval
        self.last_called = {}

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_id = id(func)
            current_time = time.time()
            if func_id not in self.last_called:
                self.last_called[func_id] = current_time
                return func(*args, **kwargs)
            elapsed = current_time - self.last_called[func_id]
            if elapsed >= self.min_interval:
                self.last_called[func_id] = current_time
                return func(*args, **kwargs)
            else:
                remaining = self.min_interval - elapsed
                print(f"Function '{func.__name__}' is rate-limited. Try again in {remaining:.2f} seconds.")
        return wrapper
