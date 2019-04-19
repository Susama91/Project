def odd_index(str1):
    res=""
    for p in range(len(str1)):
        if p%2==0:
            res=res+str1[p]
    print(res)
odd_index("susama")       
odd_index("mahi")
