def linear_search(lst, to_find):
  # search for the element to_find inside lst
  lst = lst.sorted()
  for i in range(0,len(lst)):
      if lst[i] == to_find:
          return i 
  return -1
    

                
  # if found, return index of element
  # else return -1
