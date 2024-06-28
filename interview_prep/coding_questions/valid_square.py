#  13. Given a positive integer num, write a function that returns True if num is a perfect square else False.
"""
This has a relatively straightforward solution. You can check if the number has a perfect square root by:

Finding the square root of the number and converting it into an integer.
Applying the square to the square root number and checking if it's a perfect square root.
Returning the result as a boolean. 
"""


def valid_square(num):
    square = int(num**0.5)
    return (square**2) == num


print(valid_square(10))
# False
print(valid_square(36))
# True
