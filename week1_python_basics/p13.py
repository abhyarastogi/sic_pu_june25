def printing_hollow_rhombus(size):
    for i in range(1,size+1):
        if i == 1:
            print(' ' * (size-1) + '*' * size)
        elif i == size:
            print('*' * size)
        else:
            print(' '*(size-i) + '*' + ' '*(size-2) + '*')         
n = int(input('Enter Size :'))
printing_hollow_rhombus(n)