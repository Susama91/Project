print("begin")
try:
    x=int(input("enter fno"))
    y=int(input("enter sno"))
    z=x/y
    print(z)
    raise ValueError
except(ZeroDivisionError):
    print("sno can not be zero")
except(ValueError):
    print("enter numerical  number only")
except:
    print("error occured")    
print("end")    
