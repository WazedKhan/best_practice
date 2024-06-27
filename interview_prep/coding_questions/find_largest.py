# Question 3: Write a Python program to find the largest element in a list.


def find_largest(numbers):
    # take the first element
    current_largest = numbers[0]

    for number in numbers:
        if number > current_largest:
            current_largest = number

    return current_largest


# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")
# O(n) time complexity
