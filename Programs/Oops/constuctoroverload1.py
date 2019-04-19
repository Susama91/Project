class x:
    def __init__(self):
        self.a=1000
        self.b=2000
class y(x):
    def __init__(self):
        self.c=3000
        self.d=4000
        super().__init__()
y1=y()
print(y1.a)
print(y1.b)
print(y1.c)
print(y1.d)
        
        
