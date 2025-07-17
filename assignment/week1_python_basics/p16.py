# Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
def sum_of_series(n, m):
    sum=0
    denominator = 1
    sign = 1
    for i in range(m):
        numerator= n**2**i
        sum += (sign*numerator)/denominator
        sign *= -1
        denominator += 2
    print('Sum of series:',sum)
a,b = input('Enter value of n and number of terms m where 1<=n<=4 and 2<=m<=10').split()
a = int(a)
b = int(b)
sum_of_series(a, b)