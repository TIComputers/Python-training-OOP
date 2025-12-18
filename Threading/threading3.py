from threading import Thread, current_thread
from time import time, sleep

def task():
        print(f"Thread {current_thread().name}")
        
t1 = Thread(target=task, name="Thread_A")
t2 = Thread(target=task, name="Thread_B")

t1.start()
t2.start()

t1.join()
t2.join()
