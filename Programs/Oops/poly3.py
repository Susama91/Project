class x:
    def add(self,instanceof,*args):
        if instanceof=='int':
           result=0
        if instanceof=='str':
          result=''
        for i in args:
         result=result+i
         print(result)
x1=x()
x1.add('int',10,20,30)
x1.add('str','lokeshit','python')
         
