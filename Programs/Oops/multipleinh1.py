class x:
 def m1(self):
     print("in m1 of x")
class y:
 def m1(self):
     print("in m1 of y")
class z(x,y):
 def m3(self):
     print("in m3 of z")
z1=z()
p=z1.__hash__()
print(p)
z1.m1()
z1.m3()
