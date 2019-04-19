import re
regex=r"[a-zA-Z]+ \d+"
m=re.findall(regex,"june 24, july 25, August 14, Feb")
for i in m:
    print("match month:",i)
