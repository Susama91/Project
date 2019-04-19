class cust:
 """cust app"""
 cbname="sbi"
 def __init__(self,cname,cadd,cacno,cbal):
     self.cname=cname
     self.cadd=cadd
     self.cacno=cacno
     self.cbal=cbal
 def __str__(self):
     return self.cname+" "+self.cadd+" "+str(self.cacno)+" "+str(self.cbal)+" "+cust.cbname
 def deposit(self,damt):
     self.cbal=self.cbal+damt
 def withdraw(self,wamt):
     self.cbal=self.cbal-wamt
 def display(self):
     print(self.cname)
     print(self.cadd)
     print(self.cacno)
     print(self.cbal)
c1=cust("smith","dallas",1001,3000.00)
print(c1)
c2=cust("blake","chennai",1002,3500.00)
print(c2)
c3=cust("miller","mumbai",1003,4000.00)
print(c3)
print(".......")
x=[c1,c2,c3]
for p in x:
    print(p)
    x.sort(key=lambda c:c.cname,reverse=True) 
for q in x:
    print(q)
