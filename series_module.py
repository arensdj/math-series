def fibonacci(n):
  # n = int(input())
  array = []
  index = 1
  array.append(index)
  array.append(index)
  total = 0

  while (index < n):
    total = array[index -1] + array[index]
    array.append(total)
    index += 1

  print(str(array[index - 1]))

  return array
