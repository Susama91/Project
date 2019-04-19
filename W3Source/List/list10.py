#Write a Python program to find the list of words that are longer than n
#from a given list of words.
def lword(str1,n):
    x=[]
    txt=str1.split()
    for i in txt:
        if len(i)>n:
            x.append(i)
    print(x)
lword('python is a open',2)     
            
