def strly(str1):
    length=len(str1)
    if length>2:
        if str1[-3:]=='ing':
            str1=str1+'ly'
        else:
            str1=str1+'ing'
    print(str1)
strly('abc')
strly('string')
strly('ma')

