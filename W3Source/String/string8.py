def word(str1):
    leng=[]
    for p in str1:
        leng.append((len(p),p))
    #print(leng)
    leng.sort()
    print(leng[-1][1])
        #print(p)
    #print(str1)
word(["python", "is", "easy","to","learn"])
