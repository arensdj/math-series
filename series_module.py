def fibonacci(n):
  array = []
  index = 1
  array.append(index)
  array.append(index)
  total = 0

  for i in range(index, n):
    total = array[i - 1] + array[i]
    array.append(total)
    
  return array[i]

def lucas(n):
  array = []
  index = 1
  array.append(index+1)
  array.append(index)
  total = 0

  for i in range(index, n):
    total = array[i -1] + array[i]
    array.append(total)
  
  # print(str(array))
  # print(str(array[i]))
  return array[i]


def sum_series(n, arg1=0, arg2=1):
  array = []
  total = 0
  index = 1

  # if optional arguments are not included in function call, produce
  # fibonacci numbers
  if ( (arg1 == 0) and (arg2 == 1) ):
    array.append(index)
    array.append(index)
  else:
  # optional numbers were included in function call.  Produce lucas numbers
    array.append(index+1)
    array.append(index)

  for i in range(index, n):
    total = array[i - 1] + array[i]
    array.append(total)
    
  return array[i]
  

