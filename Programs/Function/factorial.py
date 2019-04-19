def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
num=int(input("enter a positive no"))
if num>=1:
    res=fact(num)
print("factorial of a number is:",res)    
