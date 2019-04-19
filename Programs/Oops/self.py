class x:
    def m1(self,a):
        print(self)
        print(a)
    def m2(p,q):
        print(p)
        print(q)
x1=x()
print(x1)
x1.m1(1000)
x1.m2(2000)
x2=x()
print(x2)
x2.m1(1234)
x2.m2(5678)
