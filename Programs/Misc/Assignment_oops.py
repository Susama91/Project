class Account:
    balance=0
    def __init__(self,balance):
        if balance>=0:
            Account.balance=balance
        else:
            Account.balance=0.0
            print("balance can not be negative")
    def credit(self,amt):
        if amt>0:
            Account.balance=Account.balance+amt
            return Account.balance
        else:
            print("credited amt must be greater than zero")
    def debit(self,amt):
        if (Account.balance-amt)>=0:
            Account.balance=Account.balance-amt
            return Account.balance
        else:
            print("Debit amount exceeded account balance")
    def getBalance(self):
        return Account.balance

class Savingsaccount(Account):
    def __init__(self,interestRate):
        self.balance=Account.getBalance(self)
        self.interestRate=interestRate
    def calculateinterest(self):
        self.balance=self.balance+(self.balance*self.interestRate)/100
        Account.balance=self.balance

class Checkingaccount(Account):
    def __init__(self,fee):
        self.balance=Account.getBalance(self)
        self.fee=fee
        
    def credit(self,amt):
        if amt>0:
            Account.balance=Account.balance+amt 
            print(Account.balance)
            Account.balance=Account.balance-self.fee
        else:
            print("credited amt must be greater than zero")
        
    def debit(self,amt):
        if (self.balance-amt)>=0:
            Account.balance=Account.balance-amt
            print(Account.balance)
            Account.balance=Account.balance-self.fee
        else:
            print("Debit amount exceeded account balance")

        
    
class Currentaccount(Account):
    def __init__(self):
        self.balance=Account.getBalance(self)
        self.mol=5000    
    def debit(self,amt):
        if self.mol>=amt:
            super().debit(amt)  
        else:
            print("maximum of overdraft limit reached")
    
if __name__=='__main__':
            a=Account(100)
            print("account balance is",a.getBalance())
            j=Savingsaccount(5)
            j.calculateinterest()
            print("account balance after calculate intrest",a.getBalance())
            ob=Checkingaccount(1)
            ob.credit(50)
            print("account balance after credit transaction",a.getBalance())
            ob.debit(50)
            print("account balance after debit transaction",a.getBalance())
            y=Currentaccount()
            y.debit(50)
            print("account balance after debit transaction ",a.getBalance())
            y.credit(50)
            print("account balance after credit transaction ",a.getBalance())
