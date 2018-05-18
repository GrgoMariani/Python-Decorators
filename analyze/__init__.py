__all__ = ["analyze_number_of_calls", "analyze_time_of_execution", "print_analysis", "restart_analysis"]
import time
from functools import wraps

num_of_calls = dict()
time_of_calls = dict()


def analyze_number_of_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if str(func) not in num_of_calls:
            num_of_calls[str(func)] = 0
        num_of_calls[str(func)] = num_of_calls[str(func)]+1
        return func(*args, **kwargs)
    return wrapper


def analyze_time_of_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if str(func) not in time_of_calls:
            time_of_calls[str(func)] = 0
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time()-start
        time_of_calls[str(func)] = time_of_calls[str(func)]+duration
        return result
    return wrapper


def print_analysis():
    print("\n\n ... analyzing ...")
    if len(num_of_calls) > 0:
        print(" ---> MOST CALLED")
        for item in sorted(num_of_calls, key=num_of_calls.get, reverse=True):
            print(str(item)+" | "+str(num_of_calls[item])+" times called ")
    if len(time_of_calls) > 0:
        print(" ---> MOST TIME CONSUMING")
        for item in sorted(time_of_calls, key=time_of_calls.get, reverse=True):
            print(str(item)+" | "+str(time_of_calls[item])+" seconds ")


def restart_analysis():
    num_of_calls.clear()
    time_of_calls.clear()
