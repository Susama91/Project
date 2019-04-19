import re
regex=re.compile(r"[a-zA-Z]+")
fp=open("emp.txt")
data=fp.read()
res=regex.findall(data)
for i in res:
    print(i)
