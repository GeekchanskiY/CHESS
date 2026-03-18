import time
from functools import wraps
from logging import debug


def available_moves_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.perf_counter()

        turn = kwargs.get("turn")
        if turn is None and len(args) > 1:
            turn = args[1]

        result = func(self, *args, **kwargs)

        elapsed = (time.perf_counter() - start) * 1000
        debug(f"{type(self).__name__}.{func.__name__} turn={turn} time={elapsed:.3f}ms")

        return result

    return wrapper
