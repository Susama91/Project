dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1
 
calc = 0
for k in dictionary:
    calc += dictionary[k]
 
print (calc)
