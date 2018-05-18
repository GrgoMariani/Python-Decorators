__all__ = ["ternary", "ternary_call"]


def ternary(return_value_true, return_value_false):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result:
                return return_value_true
            return return_value_false
        return wrapper
    return wrapper2


def ternary_call(func_true, func_false):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result:
                return func_true()
            return func_false()
        return wrapper
    return wrapper2


