class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
number=10
while True:
    try:
        num=int(input("enter a number"))
        if num<number:
            raise ValueTooSmallError
        elif num>number:
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print("the value is too small, please try again")
    except(ValueTooLargeError):
        print("the value is too large, please try again")
print("you ahev guessed correctly")    
    
