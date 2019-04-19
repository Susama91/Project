# Write a Python program to print the numbers of a specified list
#after removingeven numbers from it.

x=[10,11,12,13,14,15,16]
y=[]
for i in x:
    if i%2!=0:
        y.append(i)
print(y)        
