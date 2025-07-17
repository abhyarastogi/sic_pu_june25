#Find sum of the Even placed digits in the given number
def finding_sum_even_placed(n):
    sum = 0
    size = len(n)
    for i in range(1, size+1):
        if i % 2 == 0:
            sum += int(n[i-1])
    print(sum)
input_number = input('Enter the number :')
list1 = list(input_number)
finding_sum_even_placed(list1)