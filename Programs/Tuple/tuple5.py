x=((10,20,30),[40,50,60],(70,80,90))
print(x)
for p in x:
    print(p,type(p))
x[1][1]=100
for q in x:
    print(q)        
y=(i for i in range(10))
print(y)
