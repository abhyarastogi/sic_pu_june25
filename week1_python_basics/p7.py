#Find the second smallest digit in a number
input_number = input('Enter a number :')
min = 9
for i in input_number:
    if int(i) < int(min):
        min = i