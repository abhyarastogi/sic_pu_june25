#Find Factorial of a number
def finding_factorial(n):
    if n > 1:
        return n * finding_factorial(n-1)
    else:
        return 1
input_number = int(input('Enter a number:'))
result = finding_factorial(input_number)
print('Factorial of',input_number,':',result)