import re
regex=r"[a-zA-Z]+ \d+"
m=re.finditer(regex,"june 24, july 25, august 17, feb")
for i in m:
    print("match index at:",i.start(),i.end())
