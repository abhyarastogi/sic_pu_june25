#Accpet a number from the user (4 digit number where a digit can repeat at most 2 times )and print the coutn of recursions reqired to arrive at Karpekar's Constant.
def counting_recursions(num):
    count = 0
    while num != 6174:
        num_str = str(num)
        decending = int(''.join(sorted(num_str, reverse = True)))
        ascending = int(''.join(sorted(num_str)))
        num = decending - ascending
        count += 1
    print('Count of recursions are:',count)
input_number =input('Enter a 4 digit number where a digit can repeat at most 2 times : ')
counting_recursions(input_number)