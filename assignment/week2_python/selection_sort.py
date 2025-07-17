def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current index is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update minimum index
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
