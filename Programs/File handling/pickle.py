import pickle
data=[["scott",7788,3000.00],
      ["blake",7902,2500.00],
      ["smith",7369,4000.00]]
x=open("picfile.txt","wb")
pickle.dump(data,x)
x.close()
