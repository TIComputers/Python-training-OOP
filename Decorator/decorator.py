from datetime import datetime

def Time(func):
    from colorama import Fore
    def wraper():
        start = datetime.now()
        func()
        stop  = datetime.now()
        print(f"{Fore.GREEN}Time Runing: {Fore.YELLOW}{stop - start}{Fore.RESET}")
    return wraper


def Log(func):
    def wraper():
        a = func()
        print(f"log -> {a}")
    return wraper


@Time
@Log
def loop():
    print("fun loop is runing...")
    for i in range(100000):
        print(f"\r{i}", end="")
    print()
    return "loop"
    

loop()
