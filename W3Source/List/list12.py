#Write a Python program to print a specified list after removing
#the 0th, 4th and 5th elements.
#['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#['Green', 'White', 'Black']

x=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#obj1=enumerate(x)
#print(x)
#print(list(enumerate(x)))
lst=[]
for i in x:
    if x.index(i) not in (0,4,5):
        lst.append(i)
print(lst)
    
