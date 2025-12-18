from threading import Thread, Lock
from time import time
lock = Lock()

couter = 0

def increment():
    global couter
    for _ in range(10000000):
        with lock: # with lock time: 4.024
            couter += 1 # without lock time: 14.128
        
t1 = Thread(target=increment)
t2 = Thread(target=increment)
t3 = Thread(target=increment)
t4 = Thread(target=increment)
t5 = Thread(target=increment)
t6 = Thread(target=increment)
t7 = Thread(target=increment)
t8 = Thread(target=increment)

start = time()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

print(f"time: {time() - start:.3f}")
print("Counter", couter)
