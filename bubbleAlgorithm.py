array = [10, 2, 5, 6, 8, 1]

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]




































array.sort()
print(array)