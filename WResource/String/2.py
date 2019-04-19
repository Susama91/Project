"""2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""

def countchr(x):
    p={}
    for k in x:
        keys=p.keys()

        if k in keys:
            p[k]+=1
        else:
            p[k]=1
    print(p)            
        
        
    
x='google'
countchr(x)
