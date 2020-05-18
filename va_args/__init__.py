__all__ = ["va_args", "va_args2"]
from functools import wraps


def va_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        format_string = args[0]
        other_args = args[1:]
        string = format_string % other_args
        result = func(string)
        return result
    return wrapper


def va_args2(num_args):
    """
    Same as va_args, but sometimes format string comes after other arguments
    @va_args2(0) is same as @va_args
    """
    def wrapper_out(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            before_args = args[:num_args]
            format_string = args[num_args]
            other_args = args[num_args+1:]
            string = format_string % other_args
            result = func(*before_args, string)
            return result
        return wrapper
    return wrapper_out
