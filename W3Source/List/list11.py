# Write a Python function that takes two lists and returns True if they have
#at least one common member.
lst1=[10,20,30]
lst2=[30,40,40]
result=False
for p in lst1:
    for q in lst2:
        if p==q:
            #print("True")
            result=True
            print(result)
       
            
