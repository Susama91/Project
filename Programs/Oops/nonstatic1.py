class test:
 """ non static variable example"""
 def insert(self):
     self.a=1000
     self.b=2000
 def display(self):
     print(self.a)
     print(self.b)
t1=test()
t1.insert()
t1.display()
print(t1.a)
print(t1.b)
