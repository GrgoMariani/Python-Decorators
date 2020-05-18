import inspect

__all__ = ["TODO"]

todo_map = dict()


def TODO(func):
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(inspect.currentframe().f_back)
    todo_map[func.__name__] = [line_number, filename]

    def wrapper(*args, **kwargs):
        print("-------------------------------------------------------------")
        print("\tSorry. The function '{}' is still in development.  :(".format(func.__name__))
        print("\tLine {} in {}".format(line_number, filename))
        print("\tAlso registered {} other TODOs".format(len(todo_map)))
        print("-------------------------------------------------------------")

    return wrapper
