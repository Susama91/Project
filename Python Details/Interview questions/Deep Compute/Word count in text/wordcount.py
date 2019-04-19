fname = input("Enter file name: ")
word=input("Enter word to be searched:")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        #print(words)
        for i in words:
            #print(i)
            if(i==word):
                k=k+1
print("Occurrences of the word:")
print(k)
