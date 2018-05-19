__all__ = ["change_args", "change_function"]
from functools import wraps


def change_args(*args, **kwargs):
    def wrapper2(func):
        @wraps(func)
        def wrapper(*args_we_dont_need, **kwargs_we_dont_need):
            return func(*args, **kwargs)
        return wrapper
    return wrapper2


def change_function(func):
    @wraps(func)
    def wrapper2(func_we_dont_need):
        @wraps(func_we_dont_need)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return wrapper2
