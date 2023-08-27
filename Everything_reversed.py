def everything_reversed(my_list):
  list_2 = []
  j = len(my_list)-1
  #reversing element of a list
  for i in my_list:
    k=i[::-1]
    list_2.append(k)
  #reversing a list
  list_3 = []
  while j >= 0:
      a = list_2[j]
      list_3.append(a)
      j=j-1
    
  return list_3
      

if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list) 
