class x:
 a=1000
 def m1(self):
     print("in m1 of x")
class y(x):
 c=3000
 def __init__(self):
     self.d=4000
 def m2(self):
      print("in m2 of y")
 def display(self):
      print(y.c)
      print(self.d)
      self.m2()
      print(y.a)
      self.m1()
y1=y()
y1.display()     
