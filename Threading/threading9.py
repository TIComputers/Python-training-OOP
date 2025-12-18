import threading
import time

event = threading.Event()

def task1():
    print("task 1 watting for event")
    event.wait()
    print("task 1 started")

def task2():
    print("task 2 running")
    time.sleep(2)
    print("task 2 setting event")
    event.set() # send signal to continue task1


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

