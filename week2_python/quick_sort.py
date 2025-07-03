def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index + 1, high)
def partition(array, low, high):
    pivot = array[high]
    k = low
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[k] = array[k], array[i]
            k += 1
    array[k], array[high] = array[high], array[k]
    return k
array = [3, 7, 9, 1, 5]
quick_sort(array, 0, len(array)-1)
print(array)