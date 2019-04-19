#2. Write a Python program to multiplies all the items in a list

def mul(n):
    s=1
    for p in n:
        s=p*s
    print("the result is :", s)

mul([10,20,30])

