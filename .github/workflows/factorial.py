#  Initial Python code to calculate the factorial of a number. Here's a simple example:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")
