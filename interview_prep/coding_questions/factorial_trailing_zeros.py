# 14. Given an integer n, return the number of trailing zeroes in n factorial n!
"""
To pass this challenge, you have to first calculate n factorial (n!) and then calculate the number of training zeros. 

Finding factorial 
In the first step, we will use a while loop to iterate over the n factorial and stop when the n is equal to 1. 

Calculating trailing zeros
In the second step, we will calculate the trailing zero, not the total number of zeros. There is a huge difference. 
"""


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def factorial_trailing_zeros(n):
    result = factorial(n)
    zero_counter = 0

    for i in str(result)[::-1]:
        if i == "0":
            zero_counter += 1
        else:
            break
    return zero_counter


print(factorial_trailing_zeros(10))  # 2
print(factorial_trailing_zeros(18))  # 3
