from threading import Thread
from time import time, sleep
from random import choice

def download_file(file_id, delay):
    print(f"start download file {file_id}")
    sleep(delay)
    print(f"finish download file {file_id} time:({delay})")
    
times = [1, 3, 6, 10]
threads = []
for i in range(5):
    t = Thread(target=download_file, args=(i, choice(times)))
    t.start()
    threads.append(t)

print("-" * 20)

for t in threads:
    t.join()
    
print("all file downloaded")
