class x:
 def m1(self):
     print("in m1 of x")
 def m2(self):
     print("in m2 of x")
class y(x):
 def m1(self):
     print("in m1 of y")
 def m3(self):
     print("in m3 of y")
 def display(self):
     self.m1()
     self.m2()
     self.m3()
     super().m1()
y1=y()
y1.display()
     
