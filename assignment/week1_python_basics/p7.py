#Find the second smallest digit in a number
input_number = input('Enter a number :')
min1 = 9
min2 = 9
for i in input_number:
    if int(i) < int(min1):
        min2 = min1
        min1 = i
    elif int(i) > int(min1):
        min2 = i
print('The second smallest digit is:',min2)