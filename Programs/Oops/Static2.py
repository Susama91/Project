class test:
 """ static variable example"""
 a=1000
 b=2000
 def display(self):
     print(test.a)
     print(test.b)
 def modify(self):
        test.a=test.a+100
        test.b=test.b-100
          
t1=test()
t1.display()
t1.modify()
t1.display()
t2=test()
t2.display()
t2.modify()
t3=test()
t3.display()
          
