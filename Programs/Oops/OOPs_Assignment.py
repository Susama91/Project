class Account:
    """ Account Class"""
    acc_bal=0
    def __init__(self,ini_bal):
        self.ini_bal=ini_bal
        Account.acc_bal=Account.acc_bal+ini_bal
        print(Account.acc_bal)
        if Account.acc_bal >= 0:
            Account.acc_bal=Account.acc_bal
            print("Initial Balance is",Account.acc_bal)
        else:
            Account.acc_bal=0
            print("Initial balance was invalid")
    def credit(self,credit_amt):
        if credit_amt >0:
            Account.acc_bal=Account.acc_bal+credit_amt
            print("After crediting the amount Account balance is:",Account.acc_bal)
            return True
        else:
             print("The credit Amount should be positive Amount")
             return False
    def debit(self,debit_amt):
        if Account.acc_bal < debit_amt:
            print("Debit Amount Exceeded the Account Balance")
            return False
        else:
            Account.acc_bal=Account.acc_bal-debit_amt
            print("After Debiting amount Account balance is:",Account.acc_bal)
            return True
    def getBalance(self):
        print("Current Balance is:",Account.acc_bal)
        return Account.acc_bal
        
class SavingAccount(Account):
    """ Saving Account Class"""
    Interesr_Rate=0
    def __init__(self,ini_bal,Interest_Rate):
        self.ini_bal=ini_bal
        Account.acc_bal=self.ini_bal+self.getBalance()
        SavingAccount.Interest_Rate=Interest_Rate
        #print(Account.acc_bal)
    def calculateinterest(self):
        Account.acc_bal=Account.acc_bal+(Account.acc_bal * SavingAccount.Interest_Rate)/100
        print("The Account Balance after adding interest is:",Account.acc_bal)
  
class CheckingAccount(Account):
    """ Checking Account Class"""
    fee_amt=0
    def __init__(self,ini_bal,fee_amt):
        self.ini_bal=ini_bal
        Account.acc_bal=self.ini_bal+self.getBalance()
        CheckingAccount.fee_amt=fee_amt
        if CheckingAccount.fee_amt >0:
            CheckingAccount.fee_amt = CheckingAccount.fee_amt
        else:
            print("The Fee Amount should be positive Amount")
    def credit(self,credit_amt):
        if Account.credit(self,credit_amt):
            Account.acc_bal=Account.acc_bal-CheckingAccount.fee_amt
            print("The Account Balance after debiting Fee Amount is:",Account.acc_bal)
        else:
            print("Fee Cant be charged")
    def debit(self,debit_amt):
        if Account.debit(self,debit_amt):
            Account.acc_bal=Account.acc_bal-CheckingAccount.fee_amt
            print("The Account Balance after debiting Fee Amount is:",Account.acc_bal)
        else:
            print("Fee Cant be charged")       
class CurrentAccount(Account):
    """ Current Account """
    pass
#a1=Account(2000)

sa=SavingAccount(5000,6)
sa.credit(5000)
sa.debit(2000)
#ac=SavingAccount(6)
sa.calculateinterest()
#ac.getBalance()
ca=CheckingAccount(5000,25)
ca.credit(5000)
ca.debit(2000)
ca.getBalance()

