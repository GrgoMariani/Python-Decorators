__all__ = ["for_each_elem"]

from functools import wraps


def for_each_elem(some_list):
    def wrapper2(func):
        @wraps(func)
        def wrapper():
            result = []
            for element in some_list:
                result.append(func(element))
            return result
        return wrapper
    return wrapper2
