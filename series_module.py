# This function produces the fibonacci Series which is a numeric series starting 
# with the integers 0 and 1. In this series, the next integer is determined by 
# summing the previous two.  
# The resulting series looks like 0, 1, 1, 2, 3, 5, 8, 13, ...
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

# This function produces the Lucas Numbers.  This is a related series of integers 
# that start with the values 2 and 1.  
# This resulting series looks like 2, 1, 3, 4, 7, 11, 18, 29, ...
def lucas(n):
  array = []
  index = 1
  array.append(index+1)
  array.append(index)
  total = 0

  for i in range(index, n):
    total = array[i -1] + array[i]
    array.append(total)
  
  return array[i]

# This function produces numbers from the fibonacci series if there are no
# optional parameters.  Invoking this function with the optional arguments 2 and 1
# will produce values from the lucas numbers. 
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
  