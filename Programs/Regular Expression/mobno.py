import re
regex=re.compile(r"\d{10}")
while True:
    mobno=input("enter a mobile number")
    if len(mobno)==10:
       result=regex.search(mobno)
       if result:
           print("valid mob no")
           break
       else:
           print("mob no should contsin digits only")
    else:
        print("mob no should be 10 digit")
        
