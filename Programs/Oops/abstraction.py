class x:
    __a=100
    def __init__(self):
        self.__b=2000
    def m1(self):
        print("in m1 of x")
    def display(self):
        print(x.__a)
        print(self.__b)
        self.__m1()
x1=x()
x1.display()
print(x1.__a)
print(x1.__b)
x1.__m1()

        
