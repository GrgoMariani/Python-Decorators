from do_in_main_thread import do_in_main_thread, executeTask
import threading
import time
""" Shorter:
        Some people really fear MultiThreading. I would honestly recommend you spend some time learning about 
            threads than resort to using this code.
            This example is mainly put here so you can get some inspiration for some programming patterns. 

    Short:
        @do_in_main_thread puts function on a stack to be executed in the main_thread via executeTask() function
        
        executeTask() executes functions that were called from this or other threads to be executed in this thread.
"""


class ThisIsDoneInAnotherThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("\nStarting @ {}".format(threading.current_thread()))
        print_current_thread()
        print("Exiting @ {}".format(threading.current_thread()))


@do_in_main_thread
def print_current_thread():
    print("\n       Current thread is {}".format(threading.current_thread()))


if __name__ == '__main__':
    while True:
        ThisIsDoneInAnotherThread().start()
        executeTask()
        time.sleep(3)
