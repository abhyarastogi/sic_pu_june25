# Print N Fibo terms with 1 and 2 as 1st 2 terms.
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n - 1) + fibo(n - 2)
n = int(input("Enter number of terms: "))
print(f"\nFirst {n} terms of the Fibonacci series (starting with 1, 2):")
for i in range(1, n + 1):
    print(fibo(i), end=" ")
