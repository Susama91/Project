x=[10,20,30,40,50,60]
print(x)
s=0
for p in x:
    print(p)
    s=s+p
print("using for loop sum is:",s)

t=0
i=0
while i<len(x):
    print(x[i])
    t=t+x[i]
    i=i+1
print("using while loop sum is:",t)
    
    
