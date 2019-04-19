class x:
 def m1(self):
     print("in m1 of x")
class y(x):
 def m2(self):
     print("in m2 of y")
     print(x.__bases__)
     print(y.__bases__)
y1=y()
y1.m1()
y1.m2()
p=y1.__hash__()
print(p)
