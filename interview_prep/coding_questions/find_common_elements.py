# Question 7: Write a Python program to find the common elements between two lists.


def find_common_elements(list1, list2):
    common_element = []
    for item in list1:
        if item in list2:
            common_element.append(item)
    return common_element


# Test the function
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)
