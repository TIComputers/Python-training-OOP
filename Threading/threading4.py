from threading import Thread, active_count, enumerate
from time import time, sleep


def task():
    sleep(1)
    
threads = []
for i in range(5):
    t = Thread(target=task, name=f"Thread_{i}")
    t.start()
    threads.append(t)
    
print("number active thread: ", active_count())

for j in enumerate():
    print(j.name)

for t in threads:
    t.join()

