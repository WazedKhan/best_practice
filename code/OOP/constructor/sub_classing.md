# Sub-classing Python's / Extending Built-in Immutable Classes in Python:

Have you ever needed to extend the functionality of Python's built-in immutable classes like `float`, `int`, or `str`? Whether you want to add additional features or create a similar custom class with more functionalities, Python allows you to do just that and its calls sub classing in python.

### What we will discuss in this article:

* **Introduction to Sub-classing Built-in Types** : A brief overview of why and when you might want to subclass built-in immutable types like `float`.
* **Scenario Explanation** : Discuss a specific scenario where we need to work with distances in our application and want to leverage the existing functionality of the `float` type while also maintaining the unit of measurement.
* **Basic Implementation Attempt** : Show a naive implementation attempt of sub-classing `float` and explain why it fails due to the immutable nature of built-in types.
* **Understanding the TypeError** : Provide a detailed explanation of why the `TypeError` occurs when trying to subclass and initialize an immutable type like `float`.
* **Correcting the Approach with `__new__`** : Introduce the `__new__` method, explaining its role in creating instances of immutable types and how it differs from `__init__`.
* **Example Implementation Using `__new__`** : Provide a corrected implementation of the `Distance` class using the `__new__` method to properly subclass `float` and add additional attributes.
* **Explanation of Corrected Code** : Break down the corrected implementation step-by-step, highlighting key points and demonstrating how the class can be used in practice.

### What is sub-classing:

If you are familiar with OOP, you probably already understand subclassing. To refresh the concept, subclasses are classes that inherit from a parent class. This means that each child class can utilize the methods and variables of the parent class.

### **Scenario Explanation**

Given the scenario where we need to work with distances in our application and want to leverage the existing functionality of the `float` type while also maintaining the unit of measurement, sub-classing `float` is a good solution. This approach allows us to extend `float` to include the unit and provide additional functionality specific to distances.

## lets try out the basic implementation by ignoring that float it immutable class

```python
1 class Distance(float):
2     def __init__(self, value, unit):
3        super().__init__(value)
4        self.unit = unit

output:
---------------------------------------------------
in_miles = Distance(42.0, "Miles")
output:
TypeError: float expected at most 1 argument, got 2
```

## Understanding the TypeError

so when we subclass a built-in immutable type like float, Python expects us to initialize the instance during its creation using the `__new__` method. Here's why:

NOTE: **In Python, immutable types such as float, int, and tuple do not allow their instances to be modified after they are created. This immutability is enforced to ensure the consistency and integrity of these fundamental types.**

### Error Cause:

- In our code, we tried to use `super().__ init __(value)` in the `__ init __` method of Distance. However, float does not accept multiple arguments in its constructor because it expects only one argument (the numerical value).
- This mismatch between the number of arguments (value and unit) and what float expects led to the TypeError.

### Immutable Nature:

- Immutable types cannot have their state changed after creation. This means attributes cannot be added or modified after the instance is instantiated.
- Since float objects are immutable, their value cannot be changed once they are created. Therefore, the `__ init __` method, which is called after the instance is created, cannot be used to modify the object's state.

### `__new__` vs `__init__`:

1. `__ new __()`: Responsible for creating a new instance of the class. It's called first and returns a new object instance.
2. `__ init __()`: Initializes the created instance after it has been created by `__ new __`. It's used to set up initial attributes and state.

### Correct Approach

To correctly subclass `float` and include additional attributes like `unit`, we should override the `__new__` method to initialize the instance with both the value and the unit. Here’s the corrected approach:

```python
class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

# Example usage
if __name__ == "__main__":
    in_miles = Distance(42.0, "Miles")
    print(in_miles)  # Output: 42.0
    print(in_miles.unit)  # Output: Miles

```

### Explanation of the Corrected Code

* **`__new__` Method** :
* `super().__new__(cls, value)` calls the `__new__` method of the superclass (`float` in this case) to create a new instance with the given `value`.
* The `unit` attribute is then added to the instance (`instance.unit = unit`).
* Finally, the modified instance is returned (`return instance`).
* **Example Usage** :
* `Distance(42.0, "Miles")` creates a new `Distance` object with a value of `42.0` and unit `"Miles"`.
* Printing `in_miles` shows `42.0`, indicating that the object behaves like a `float`.
* Accessing `in_miles.unit` retrieves the unit `"Miles"`, demonstrating that the additional attribute `unit` is correctly stored and accessible.

By using `__new__` instead of `__init__`, you align with Python's conventions for creating instances of immutable types and avoid the `TypeError` caused by attempting to pass multiple arguments to the `float` constructor.
