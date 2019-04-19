print("begin")
x=int(input("enter fno"))
y=int(input("enter sno"))
try:
    z=x/y
    print(z)
except(ZeroDivisionError):
    print("sno can not be zero")
print("end")    
