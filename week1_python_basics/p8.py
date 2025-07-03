#Count number of prime digits in a number
def counting_prime_digit(num):
    count = 0
    for i in num:
        i = int(i)
        if i > 1:
            for j in range(2,i):
                if (i%j==0):
                    break
            else:
                count+=1
    print('Number of prime digits =',count)
input_num = input('Enter Number:')
counting_prime_digit(input_num)