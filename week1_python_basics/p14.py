def printing_x_shape(size):
    if size%2==0:
        print('Inappropriate size')
    else:
        for i in range(1, size+1):
            for j in range(1, size+1):
                if j == i or j == size-i+1:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
n = int(input('Enter Size (odd number):'))
printing_x_shape(n)