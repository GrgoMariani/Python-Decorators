__all__ = ["print_me"]

from functools import wraps


def print_me(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if(len(kwargs)>0):
            print("\n{}{}{} = {}".format(func.__name__, args, kwargs, result))
        else:
            print("\n{}{} = {}".format(func.__name__, args, result))
        return result
    return wrapper

