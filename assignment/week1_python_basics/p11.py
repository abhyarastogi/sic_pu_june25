n = int(input('Enter Size: '))
if n % 2 == 0:
    n += 1
for i in range(1, n + 1, 2):      
    spaces = (n - i) // 2
    print(' ' * spaces + '*' * i)
