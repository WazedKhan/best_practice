from constructors import Point

# point = Point(21, 42)
# print(point)
""""
output:
1. Create a new instance of Point.
2. Initialize the new instance of Point.
Point(x=21, y=42)
"""

# lets call go through it like the class creates and initialization
# creates a new instance of class(Point)
# point = Point.__new__(Point)
# print(point)
"""
output: 1. Create a new instance of Point. with error after it
"""
# point.__init__(21, 42)
# print(point)
"""
output:
1. Create a new instance of Point.
2. Initialize the new instance of Point.
Point(x=21, y=42)
"""
# we call __call__ method in another class and __call__ returns then child class's __init__ method won't be get called

from ab_classes import B

b = B(42)
print(b)
