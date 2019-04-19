import re
regex="([a-zA-Z]+) (\d+)"
res=re.sub(regex,r"\2 of \1","june 24, august 14")
print(res)
