def printing_hollow_square(size):
    for i in range(1,size+1):
        if i == 1 or i ==size:
            print('*' * size)
        else:
            print('*'+' '*(size-2)+'*')
n = int(input('Ente size :'))
printing_hollow_square(n)