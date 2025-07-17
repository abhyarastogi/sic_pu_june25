def finding_p_elements(y, element_sort):
    p =int(element_sort[y]) - int(element_sort[y-1]) -1
    print('Number of elements in p :',p)
n, x, y = (input('Size of n, x, y such that n = x + y :')).split()
n = int(n)
x = int(x)
y = int(y)
element = input('Enter the elements :').split()
element = list(element)
element_sort = sorted(element)
finding_p_elements(y, element_sort)