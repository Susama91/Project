def add(*a):
    print(a)
    print(type(a))
    print(len(a))
    s=0
    for p in a:
        s=s+p
        print(s)
add()
add(1000)
add(10,20,30,40)
