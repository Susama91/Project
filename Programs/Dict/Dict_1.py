x={"java":80,"python":99,"hadoop":75,"java":75}
print(x)
print(x["python"])
print(x["hadoop"])
print(x["java"])
print("     ")

x["aws"]=67
print(x)
print("     ")

x["hadoop"]=80
print(x)
print("     ")

print("python" in x)
print(99 in x)
print("     ")

for p in x:
    print(p,x[p])
    print("     ")
