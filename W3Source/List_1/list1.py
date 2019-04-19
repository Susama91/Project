#1. Write a Python program to sum all the items in a list

def sum(n):
    s=0
    for p in n:
        s=p+s
    print("the sum is :", s)

sum([10,20,30])
