d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
key={}
x=d.values()
for i in x:
    if i not in key:
        key.append(i)
    
print(key)
#print(y)
