x={"java":[10,20,30],
   "python":[40,50,60],
   "hadoop":[70,80,90]}
kv=x.items()
for k,v in kv:
    print(k)
    for p in v:
        print(p)
