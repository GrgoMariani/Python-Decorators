__all__ = ["executeTask", "do_in_main_thread"]
import threading
from functools import wraps

tasks = []
mutex = threading.Lock()


def addTask(func):
    mutex.acquire()
    tasks.append(func)
    mutex.release()


def isTaskReadyToExecute():
    return len(tasks) > 0


def executeTask():
    if isTaskReadyToExecute():
        mutex.acquire()
        func = tasks.pop()
        mutex.release()
        func()


def do_in_main_thread(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        addTask(func)
        return func
    return wrapper
