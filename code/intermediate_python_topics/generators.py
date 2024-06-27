"""
Generators in Python are a special type of iterable, similar to lists, tuples, and dictionaries. However, unlike these data structures, generators do not store all their values in memory; instead, they generate values on the fly and yield them one at a time as needed. This makes generators particularly useful for working with large datasets or streams of data where storing all the values in memory at once would be impractical.

Key Features of Generators:
- Lazy Evaluation: Generators compute values on demand and yield them one at a time. This allows for efficient memory usage since values are only generated when needed.
- Iterators: Generators are a type of iterator and can be iterated over using a loop.
- State Preservation: Generators maintain their state between successive calls, allowing them to resume where they left off.

Creating Generators
There are two main ways to create generators in Python:

Generator Functions: These are functions that use the yield keyword to return values one at a time.

Generator Expressions: These are similar to list comprehensions but use parentheses instead of square brackets.

Generator Functions
A generator function is defined like a normal function but uses the yield statement to return values one at a time.
"""


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
# for num in counter:
#     print(num)

# print(counter.__next__()) # 1
# print(counter.__next__()) # 2

"""
In this example, count_up_to is a generator function that yields numbers from 1 to a specified maximum.

Generator Expressions
A generator expression is similar to a list comprehension but produces a generator object.
"""

squares = (x**2 for x in range(10))
for square in squares:
    print(square)

"""
Benefits of Using Generators:
- Memory Efficiency: Generators are more memory-efficient than lists, especially for large datasets, because they generate items on-the-fly without storing them in memory.
- Performance: Generators can lead to performance improvements when dealing with large datasets, as they avoid the overhead of constructing and storing large data structures.
- Readable and Maintainable Code: Generators can make code more readable and easier to maintain by abstracting the iteration logic.
"""
