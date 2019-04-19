x={"java":{"spring":90,"structs":87,"jsf":67},
   "python":{"django":99,"flask":80,"web2py":67},
    "hadoop":{"hive":90,"pig":80,"sqoop":78}}       
kv=x.items()
for k,v in kv:
       print(k)

       print("------")

       for p,q in v.items():
           print(p,q)
