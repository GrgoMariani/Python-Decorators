from do_in_main_thread import do_in_main_thread, executeTask
import threading
import time
""" Shorter:
        Some people really fear MultiThreading. I would honestly recommend you spend some time learning about 
            threads than resort to using this code.
            This example is mainly put here so you can get some inspiration for some programming patterns.
            It basically imitates switching everything to the main lane. 

    Short:
        @do_in_main_thread puts function on a stack to be executed in the main_thread via executeTask() function
        
        executeTask() executes functions that were called from this or other threads to be executed in this thread.
"""


class AnotherThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting @ {}".format(threading.current_thread()))
        while True:
            print("Called function from thread {}".format(threading.current_thread()))
            print_current_thread()
            time.sleep(3)
        print("Exiting @ {}".format(threading.current_thread()))


@do_in_main_thread
def print_current_thread():
    print("       Current thread is {}".format(threading.current_thread()))


if __name__ == '__main__':
    AnotherThread().start()
    while True:
        executeTask()
        time.sleep(0.01)
