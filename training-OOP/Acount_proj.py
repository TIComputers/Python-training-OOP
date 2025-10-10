from Bank_Acount import * 

Ali = BankAcount(1500, "Ali")
Ali.getBalance()

Sadegh = BankAcount(1000, "Sadegh")
Sadegh.deposit(500)
Sadegh.transfer(500, Ali)


Mina = IntrestRewardAccount(1000, "Mina")
Mina.deposit(100)

Kian = SavingAccount(1000, "Kian")
Kian.transfer(1000, Ali)
Kian.transfer(100, Ali)