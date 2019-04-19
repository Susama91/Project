class x:
 def m1(self):
     print("in m1 of x")
class y(x):
 def m2(self):
     print("in m2 of y")
class z(x):
 def m3(self):
     print("in m3 of z")
y1=y()
a=y1.__hash__()
print(a)
y1.m1()
y1.m2()
z1=z()
p=z1.__hash__()
print(p)
z1.m1()
z1.m3()
     
