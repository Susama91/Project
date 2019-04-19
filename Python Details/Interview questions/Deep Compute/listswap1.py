# Swap the First and Last Value of a List  #
# 
# Taking input from the user & swapped the first value with the last value
# and printed the result
# 
# Author : Susama M
# Date : 26-12-2018

# getting list of values from user 
print("Enter a list of numbers with a space between each : \n")
a = [int(x) for x in input().split()]

# length of list
n = len(a)

# taking last value from the list to a temp variable, and swaping that with the first value
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp

# printing the swapped list
print("New list with swapped values is :\n")
print(a)
