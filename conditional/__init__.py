__all__ = ["conditional"]


def conditional(function_with_condition):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            if function_with_condition():
                return func(*args, **kwargs)
            return None
        return wrapper
    return wrapper2
