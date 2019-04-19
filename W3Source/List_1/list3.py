#3. Write a Python program to get the largest number from a list.

def mx(n):
    print("before sorting:", n)
    n.sort()
    print("after sorting:", n)
    print("largest number is:", n[-1])
mx([5,85,2,3])    

def max_number(x):
    maximum=x[0]
    for i in x:
        if i > maximum:
            maximum = i
    return maximum
x = [5,85,2,3]
print(max_number(x))
