# Question 9: Write a Python program to find the second largest number in a list.
def find_second_largest(numbers):
    largest = float("-inf")
    second_largest = float("-inf")

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    return second_largest


# Test the function
nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")
