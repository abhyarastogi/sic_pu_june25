#Finding the biggest digit in the number
input_number = input('Enter a number :')
biggest_num = 0
for i in input_number:
    if int(i) > int(biggest_num):
        biggest_num = i
print('Biggest digit in the number is :',biggest_num)    

