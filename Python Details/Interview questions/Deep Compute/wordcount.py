# Count the Occurrences of a Word in a Text File #
# 
# Given file name (need relative path or absolute path), and a word to search in the file
# The program counts number of occurances of the word in the file
# 
# Author : Susama M
# Date : 26-12-2018


# getting file from the user
file = input(" Please enter the file name:")

# getting the word to search from the user
word=input("Please enter the word to be searched:")

# Count given word, line by line from the text file 
k = 0
with open(file, 'r') as f:
    for line in f:
        words = line.split()
        #print(words)
        for i in words:
            #print(i)
            if(i==word):
                k=k+1

# print the output
print("The given word \"%s\" occurred %d times in the given file" % (word, k))
