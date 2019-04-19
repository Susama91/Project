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
print(y.a)
print(y.c)
y1=y()
print(y1.d)
y1.m1()
y1.m2()


