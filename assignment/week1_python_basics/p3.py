num1, num2, num3 = (input('Enter three numbers')).split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 < num2:
    if num1 < num3:
        print(num1,'is the smallest')
if num2 < num1:
    if num2 < num3:
        print(num2,'is the smallest')
if num3 < num1:
    if num3 < num2:
        print(num3,'is the smallest')