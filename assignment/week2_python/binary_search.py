def binary_search(searched_element, array):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if searched_element == array[mid]:
            return mid
        elif searched_element < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
searched_element = int(input('Enter the element to be searched :'))
array = list(map(int, input('Enter the elements of an array :').split()))
array.sort()
result = binary_search(searched_element, array)
print(result)