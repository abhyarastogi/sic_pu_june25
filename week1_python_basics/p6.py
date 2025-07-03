#Finding the biggest digit in the number
def finding_biggest_num(number):
    biggest_num = 0
    for i in input_number:
        if int(i) > int(biggest_num):
            biggest_num = i    
    return biggest_num   
input_number = input('Enter a number :')
result = finding_biggest_num(input_number)
print('Biggest digit in the number is :',result)