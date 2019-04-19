def triangle(n):
    k=2*n-2
    p=2*n-n
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

        
    for i in range(n,0,-1):
        for j in range(0,p):
            print(end=" ")
        p=p+1
        for j in range(0,i-1):
            print("*",end=" ")
        print("\r")      
n=4
triangle(4)
        
