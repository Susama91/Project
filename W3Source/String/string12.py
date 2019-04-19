def occ(str1):
    dic={}
    words=str1.split()
    for p in words:
        #keys=dic.keys()
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1
            
    print(dic)
occ('python is very very easy')
    
