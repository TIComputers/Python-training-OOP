from colorama import Fore

class BalanceException(Exception):
    pass

class BankAcount:
    
    Green  = Fore.GREEN
    Yellow = Fore.YELLOW
    Red    = Fore.RED
    Rest   = Fore.RESET
    
 
    def __init__(self, initalAmount:int , ActName:str):
        self.balance = initalAmount
        self.actname = ActName
        
        print(self.Green + f"Account {self.actname} Created." + self.Rest)
        print(f"Balance = {self.Yellow}{self.balance:.2f}" + self.Rest)


    def getBalance(self): # show Account Bala
        print(f"\nAcount {self.actname}", end=" ")
        print(f"Balance: {self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        
        print(self.Green + f"Deposit Complete", end="\t" + self.Rest)
        self.getBalance()       
        
        
    def checkTransAction(self, amount):
        if self.balance >= amount: return 
        else :
            raise BalanceException(self.Red + f"Sorry Acount {self.actname} only Balance of ${self.balance}" + self.Rest)
     

    def withdraw(self, amount): 
        try:
            self.checkTransAction(amount)
            self.balance -= amount
            
            print(self.Yellow + f"\n Withdraw is Completed" + self.Rest)
            
        except BalanceException as Error:
            print(self.Yellow + f"\nWithdrow is intrrupted: {Error}")
            
            
    def transfer(self, amount, accName):
        try:
            print(self.Yellow + "\nTransfer Started ...")
            
            self.checkTransAction(amount)
            self.withdraw(amount)
            accName.deposit(amount) # ***
             
            print(self.Green + f"\n{5 * "*"} Transfer Completed {5 * "*"}" + self.Rest) 
            
        except BalanceException as Error:
            print(self.Yellow + f"\nTransfer is intrrupted: {Error}")




class IntrestRewardAccount(BankAcount):
    
    def deposit(self, amount): # deposit بازنویسی تابع 
        self.balance += (amount * 1.05)
        print(self.Green + "Depositd Completed" + self.Rest) 
        self.getBalance()


class SavingAccount(IntrestRewardAccount):
    
    def __init__(self, initalAmount:int , ActName:str): 
        super().__init__(initalAmount , ActName) # -->  نمیخواهیم بازنویسی بکنیم super از 
        self.fee = 5


    def transfer(self, amount, accName):
        try:
            print(self.Yellow + "\nTransfer Started ...")

            self.checkTransAction(amount + self.fee)
            self.withdraw(amount + self.fee)
            accName.deposit(amount)
            
            print(self.Green + f"Transfer {self.Yellow}${amount} {self.Green}Successfuly" + self.Rest)

        except BalanceException as Error:
            print(self.Red + f"\nTrasfer Intrrupted: {Error}" + self.Rest)