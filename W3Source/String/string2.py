def freq(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    print(dict)
freq('google.com')
freq('susama')
