from threading import Thread
from time import time, sleep


def greet(name, delay):
    print(f"{name} Starting...")
    for i in range(8):
        sleep(delay)
        print(f"Hello {name} ({i})")
        
   
t1 = Thread(target=greet, args=("sadegh", 4))
t2 = Thread(target=greet, args=("mohammad", 1))

t1.start()
t2.start()

t1.join()
t2.join() 
