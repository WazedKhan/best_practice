# Question 8: Write a Python program to sort a list of elements using the bubble sort algorithm.


def bubble_sort(elements):
    n = len(elements)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break


# Test the function
nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)
