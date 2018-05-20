__all__ = ["stack_results", "pop_result"]
from functools import wraps

stack = []


def stack_results(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        stack.append(result)
        return result
    return wrapper


def pop_result():
    if len(stack) == 0:
        return None
    return stack.pop()
