import re
x="email address are abc@gmail.com,qyx@hotmail.com,mnc@yahoo.com"
res=re.findall(r"[\w\.-]+@[\w\.-]+",x)
#for i in res:
print(res)

