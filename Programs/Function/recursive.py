i=0
def myfunc():
    print("welcome")
    global i
    i=i+1
    while i<=5:
        myfunc()
myfunc()
