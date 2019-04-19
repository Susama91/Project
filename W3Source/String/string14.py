#def com(st):
st=input("enter")
p=[word for word in st.split(",")]
#for word in p:
x=",".join(sorted(list(set(p))))
print(x)
#com(red,white,black,red,green,red)
