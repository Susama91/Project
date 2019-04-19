#5. Write a Python program to count the number of strings where the string length is 2 or more and
#the first and last character are same from a given list of strings
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

def string_count(list):
    str = []
    cnt = 0
    for p in list:
        if len(p)>=2 and p[0]==p[-1]:
                str.append(p)
                cnt += 1
                
    print(str, cnt)            
list = ['abc', 'xyz', 'aba', '1221']
string_count(['abc', 'xyz', 'aba', '1221'])
