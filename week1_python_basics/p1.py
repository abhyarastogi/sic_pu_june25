input_year = int(input('Enter the year required to check:'))
if((input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0):
    print(input_year,'is a Leap Year')
else:
    print(input_year,'is not a Leap Year')