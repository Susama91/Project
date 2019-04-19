class emp:
 """ emp app"""
 empcount=0
 def __init__(self,ename,eadd,eid,esal):
     self.ename=ename
     self.eadd=eadd
     self.eid=eid
     self.esal=esal
     emp.empcount=emp.empcount+1
 def __del__(self):
     emp.empcount=emp.empcount-1
e1=emp("scott","dallas",7788,3000.00)
e2=emp("blake","mumbai",7902,4000.00)
e3=emp("smith","hyd",7369,3500.00)
del e2
print("total no of employees are:",emp.empcount)

