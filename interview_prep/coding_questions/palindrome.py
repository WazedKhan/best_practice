# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac

# Question 1: Write a Python program to check if a string is a palindrome


def is_palindrome(string):
    revers_string = string[::-1]
    return revers_string == string


# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
