__all__ = ["set_arguments"]


def set_arguments(*args1, **kwargs1):
    def wrapper2(func):
        def wrapper(*args2, **kwargs2):
            return func(*args1, **kwargs1)
        return wrapper
    return wrapper2

