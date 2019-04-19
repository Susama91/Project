class x:
 def __init__(self):
     print("in constructor of x")
 def m1(self):
     print("in m1 of x")
class y(x):
 def m2(self):
     print("in m2 of y")
y1=y()
y1.m1()
y1.m2()

 

