#Find smallest and biggest elements in an list of n numbers.
def printing_smallest_biggest(n):
    list1 = []
    for i in range(n):
        ele = int(input('Enter list element :'))
        list1.append(ele)
    min = list1[0]
    max = list1[0]
    for i in list1:
        if i < min:
            min = i
        if i > max:
            max = i
    print('Smallest Element:',min,'\nBiggest Element :',max)
input_size = int(input('Enter size'))
printing_smallest_biggest(input_size)