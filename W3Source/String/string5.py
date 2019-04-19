def twostring(n1,n2):
    newn1=n2[:2]+n1[2:]
    newn2=n1[:2]+n2[2:]
    x=newn1+' '+newn2
    print(x)
twostring('abc','xyz')    
