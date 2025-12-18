from threading import Thread, Timer
from time import time, sleep
from queue import Queue


q = Queue()
g = 0

def producer():
    for i in range(10000000):
        # print(f"Producer: add({i})")
        q.put(i)
        
    global g
    g = 1
        

def consumer():
    while True:
        item = q.get()
        print(f"\rConsumer: processin({item})", end="")
        q.task_done()
        # if g == 1:
        #     break
    
t1 = Thread(target=producer)
t2 = Timer(3, consumer)
# t3 = Thread(target=consumer, args=("thread(2)",))

t1.start()
t2.start()
# t3.start()

t1.join()
t2.join()
# t3.join()
    
