# Question 5: Write a Python program to count the frequency of each element


def count_frequency(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency


# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)
