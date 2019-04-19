import re
regex=re.compile(r"\d{3}.\d{1}.\d{2}.\d{2}")
fp=open("ipad.txt")
data=fp.read()
res=regex.findall(data)
for i in res:
    print(i)
                 
