class Test:
 """example of static variable"""
 a=1000
 b=2000

 def display(self):
     print(Test.a)
     print(Test.b)

t1=Test()
t1.display()
print(t1.a)
print(t1.b)
print(Test.a)
print(Test.b)
    
