# Given a number, find very next possible bigger number that has all the digits of the given number.
def next_bigger_number(n):
    digits = list(str(n))
    length = len(digits)
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1  
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])

    return int(''.join(digits))
num = int(input("Enter a number: "))
result = next_bigger_number(num)
if result == -1:
    print("No bigger number with same digits exists.")
else:
    print(f"Next bigger number with same digits: {result}")
