class test:
 def display(self):
     print(self.a)
     print(self.b)
 def __init__(self,a,b):
     self.a=a
     self.b=b
t1=test(1000,2000)
t1.display()
t2=test(3000,4000)
t2.display()

