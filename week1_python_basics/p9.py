#Print the Prime numbers in decreasing order between m and n (m < n)
def printing_prime_numbers(m,n):
    for i in range(n, m-1, -1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)
a, b = input('Enter starting and ending value:').split()
a = int(a)
b = int(b)
printing_prime_numbers(a, b)
