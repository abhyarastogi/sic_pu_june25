def orange_partition(number_of_oranges, size_of_oranges):

number_of_oranges = int(input('Enter the number of oranges :'))
size_of_oranges = list(map(int, input('Enter the sizes og oranges :').split()))
size_of_oranges_sorted = sorted(size_of_oranges)
orange_partition(number_of_oranges, size_of_oranges) 