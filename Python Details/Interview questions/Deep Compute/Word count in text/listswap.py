def swapList(newList): 
    size = len(newList) 
    print("before swap list is:\n", newList)
    # Swapping  
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
      
    return newList 
      
newList = [12, 35, 9, 56, 24] 
  
print("after swap new list is:\n",swapList(newList)) 
