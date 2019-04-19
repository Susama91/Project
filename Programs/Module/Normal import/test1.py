import demo
import imp
print("welcome")
b=2000
def f2():
    print("in f2 of test")
print(b)
f2()
print(demo.a)
demo.f1()
imp.reload(demo)
