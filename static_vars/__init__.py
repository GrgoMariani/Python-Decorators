__all__ = ["static_vars"]


def static_vars(**kwargs):
    def wrapper(func):
        for key in kwargs:
            setattr(func, key, kwargs[key])
        return func

    return wrapper
