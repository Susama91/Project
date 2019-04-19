# String encryption replacing a charector by it's adjecent alphabet
# 
# The above encryption is also called 'Ceaser Cipher' Technique
# This code only works with Alphabets only, numeric value and any special charectors will give garbage values
# 
# Author : Susama M
# Date : 26-12-2018


# Function to encrypt #
# Check for the Alphabets case to swap with right alphabet
def encrypt(text): 
    # shifting by one element
    s = 1

    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i]
        # checking if there is any space to keep the sentence structure intact
        if(char == " "):
            result += " "
        # Check if given font is uppercase or lowercase #
        # Encrypt uppercase characters 
        elif(char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
# Get text to encrypt from the user # 
text = input("Enter word to be searched : ")

print("Text given is : %s" % text)
print("The encrypted text is : %s" % encrypt(text))
