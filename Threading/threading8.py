import threading

def task():
    print("Task executed...")
    
    threading.Timer(2, task).start()
    
    
task()
