x={"java":80,"python":99,"hadoop":75,"aws":75}
print(x)
k=x.keys()
for p in k:
    print(p)

v=x.values()
for q in v:
    print(q)

kv=x.items()
for i, j in kv:
            print(i,j)


for r in kv:
        print(r[0],r[1])
