class x:
 def m1(self):
     print("in m1 of x")
 def __str__(self):
     print("in m1 of x")
 def __str__(self):
     return "lokeshit"
x1=x()
print(x1)
x1.m1()
p=x1.__str__()
print(p)
