__all__ = ["set_arguments", "set_function"]


def set_arguments(*args1, **kwargs1):
    def wrapper2(func):
        def wrapper(*args2, **kwargs2):
            return func(*args1, **kwargs1)
        return wrapper
    return wrapper2

	
def set_function(func1):
    def wrapper2(func2):
        def wrapper(*args, **kwargs):
            return func1(*args, **kwargs)
        return wrapper
    return wrapper2
