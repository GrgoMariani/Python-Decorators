__all__ = ["max_refresh"]

# if using Python<3.3 check this answer
# https://stackoverflow.com/questions/1205722/how-do-i-get-monotonic-time-durations-in-python
# and replace stopwatch() with that

import time
def stopwatch():
    return time.monotonic()

stopwatches = dict()
oldresults = dict()


# key: [string], timeout: [double]
# Each function should have it's unique key

def max_refresh(key, timeout):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            if key in stopwatches:
                if stopwatch()-stopwatches[key] < timeout:
                    return oldresults[key]
                stopwatches[key] = stopwatch()
                oldresults[key] = func(*args, **kwargs)
                return oldresults[key]
            stopwatches[key] = stopwatch()
            oldresults[key] = func(*args, **kwargs)
            return oldresults[key]
        return wrapper
    return wrapper2

