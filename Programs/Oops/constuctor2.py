class test:
 def display(self):
     print(self.a)
     print(self.b)
 def __init__(self):
     print("constructor")
     self.a=1000
     self.b=2000
t1=test()
t1.display()
t2=test()
t2.display()

