list=[1,5,10,15,20,25,30,35]
for i in range(1,8):
	list[i-1]=list[i]
for i  in range(0,8):
	print(list[i], end=" ")
