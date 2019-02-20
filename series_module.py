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
  # while (index < n):
    total = array[i -1] + array[i]
    array.append(total)
    # index += 1
  
  print(str(array))
  print(str(array[i]))
  return array[i]


  # while (index < n):
  #   total = array[index -1] + array[index]
  #   array.append(total)
  #   index += 1

  # print(str(array))
  # print(str(array[index-1]))
  # return array[index-1]

# def sum_series(n, ):



n = 5
# result = fibonacci(n)
# print('Returned: ' + str(result))
result = lucas(n)



# while (index < n):
    # total = array[index -1] + array[index]
    # index += 1
    # i += 1
# print('Content: ' + str(array))
# return array[index-1]
