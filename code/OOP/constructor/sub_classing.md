# Sub-classing Python's build in immutable class (float)
    Given the scenario where we need to work with distances in our application and want to leverage the existing functionality of the `float` type
    while also maintaining the unit of measurement, sub-classing `float` is a good solution. 
    This approach allows us to extend `float` to include the unit and provide additional functionality specific to distances.

## lets try out the basic implementation by ignoring that float it immutable class
```
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
