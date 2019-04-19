class x:
 def __init__(self,msg):
     self.msg=msg
 def __str__(self):
     return self.msg
 def m1(self):
     print("in m1 of x")
x1=x("lokeshit")
print(x1)
x2=x("python")
print(x2)
x3=x("django")
print(x3)
x1.m1()

