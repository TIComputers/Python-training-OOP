from threading import Thread
from time import sleep, time

def _time(func):
    def wraper():
        start = time()
        func()
        stop  = time()
        print(f"time: {stop - start:.3f}")
    return wraper

@_time
def task1():
    for i in range(5):
        sleep(1.3)
        print(f"task1 loop{i+1}")
        
@_time  
def task2():
    for i in range(5):
        sleep(1.3)
        print(f"task2 loop{i+1}")
        
       
t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
