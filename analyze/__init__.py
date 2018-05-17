__all__ = ["add_to_analyze", "analyze", "restart_analysis", "add_to_analyze_time"]

from functools import wraps

num_of_calls = dict()
time_of_calls = dict()


def add_to_analyze(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if str(func) not in num_of_calls:
            num_of_calls[str(func)]=0
        num_of_calls[str(func)] = num_of_calls[str(func)]+1
        return func(*args, **kwargs)
    return wrapper

import time

def add_to_analyze_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if str(func) not in time_of_calls:
            time_of_calls[str(func)]=0
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time()-start
        time_of_calls[str(func)] = time_of_calls[str(func)]+duration
        return result
    return wrapper


def analyze():
    print("\n ... analyzing ...")
    if len(num_of_calls)>0:
        print(" ---> MOST CALLED")
        for item in sorted(num_of_calls, key=num_of_calls.get, reverse=True):
            print(str(item)+" | "+str(num_of_calls[item])+" times called ")
    if len(time_of_calls)>0:
        print(" ---> MOST TIME CONSUMING")
        for item in sorted(time_of_calls, key=time_of_calls.get, reverse=True):
            print(str(item)+" | "+str(time_of_calls[item])+" seconds ")

def restart_analysis():
    num_of_calls.clear()
    time_of_calls.clear()
