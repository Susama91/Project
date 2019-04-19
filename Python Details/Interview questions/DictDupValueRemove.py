#Remove duplicate values from dictionary

x={'a':1, 'b':2, 'c':1, 'd':3, 'e':2}
result={}
for key,value in x.items():
    if value not in result.values():
        result[key]=value
print(result)        
        
        
