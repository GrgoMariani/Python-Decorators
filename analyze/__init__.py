__all__ = ["add_to_analyze", "analyze", "restart_analysis"]


num_of_calls = dict()


def add_to_analyze(func):
    def wrapper(*args, **kwargs):
        if str(func) not in num_of_calls:
            num_of_calls[str(func)]=0
        num_of_calls[str(func)]=num_of_calls[str(func)]+1
        return func(*args, **kwargs)
    return wrapper


def analyze():
    for item in sorted(num_of_calls, key=num_of_calls.get, reverse=True):
        print(str(item)+" | "+str(num_of_calls[item])+" times called ")

def restart_analysis():
    num_of_calls.clear()
