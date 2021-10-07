array = [10, 2, 5, 6, 8, 1]

for i in range(len(array)//2):
  array[i], array[len(array)-i-1] = array[len(array)-i-1], array[i]

print(array)