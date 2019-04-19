
# Python code to sort the lists using the second element of sublists 
# Inplace way to sort, use of third variable 
def Sort(x): 
    l = len(x) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (x[j][1] > x[j + 1][1]): 
                tempo = x[j]
                #print(x[j])
                x[j]= x[j + 1] 
                x[j + 1]= tempo 
    return x 
  
# Driver Code 
x =[('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 
print(Sort(x)) 
