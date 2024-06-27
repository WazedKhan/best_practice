# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac
# Question 2: Write a Python program to find the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
