class test:
 """non statis variable example"""
 def insert(self):
     self.a=1000
     self.b=2000

 def display(self):
     print(self.a)
     print(self.b)
t1=test()
t1.insert()
t1.display()
t2=test()
t2.display()
