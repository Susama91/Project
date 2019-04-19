x=(10,20,30,40,50,10,20,30)
print(x)
print(20 in x)
print(123 in x)
s=0
for p in x:
    s=s+p
print(s)
i=0
t=0
while i<len(x):
    t=t+x[i]
    i=i+1
print(t)
