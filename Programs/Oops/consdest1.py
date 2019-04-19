class  x:
 def __init__(self):
     print("constuctor in x")
 def m1(self):
     print("in m1 of x")
 def __del__(self):
     print("in destructorof x")
x().m1()     
