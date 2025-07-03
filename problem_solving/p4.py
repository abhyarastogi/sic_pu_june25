def arrangement(n, boys_sort, girls_sort):
    height = sorted(boys_sort + girls_sort)
    height_sorted = []
    if girls_sort[0] < boys_sort[0]:
        height_sorted.append(girls_sort[0])
        height_sorted.append(boys_sort[0])
        for i in range(1,n):
            height_sorted.append(girls_sort[i])
            height_sorted.append(boys_sort[i])
    else:
        height_sorted.append(boys_sort[0])
        height_sorted.append(girls_sort[0])
        for i in range(1,n):
            height_sorted.append(boys_sort[i])
            height_sorted.append(girls_sort[i])
    if height == height_sorted:
        print('Yes')
    else:
        print('No')
n = int(input('Enter number of boys and girls :'))
boys_height = list(map(int,input('Enter the height of boys :').split()))
girls_height =list(map(int,input('Enter the height of girls :').split()))
boys_sort = sorted(boys_height)
girls_sort = sorted(girls_height)
arrangement(n, boys_sort, girls_sort)