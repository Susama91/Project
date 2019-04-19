final={}
def push(x):
    if x in final:
        final[x] += 1
    else:
        final[x] = 1
push('Geeky')
push('Prep')
push('Geeky')
print (len(final))
