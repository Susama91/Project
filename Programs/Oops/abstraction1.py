class x:
    __a=100
    def m1(self):
        print("in m1 of x")
class y(x):
    __b=2000
    def __m2(self):
        print("in m2 of y")   
    def display(self):
        print(y.__b)
        self.__m2()
        print(self.__a)
        self.__m1()
y1=y()
y1.display()


        
