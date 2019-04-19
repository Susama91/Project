print("begin")
try:
    x=int(input("enter fno"))
    y=int(input("enter sno"))
    z=x/y
    print(z)
except(ZeroDivisionError):
    print("sno can not be zero")
finally:
    print("welcome") 
print("end")    
