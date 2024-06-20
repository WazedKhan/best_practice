
## Python’s Class Constructors and the Instantiation Process

### Class constructors internally trigger Python’s instantiation process, which runs through two main steps:

1. **Instance creation**
2. **Instance initialization**

- In Python, when you call a class as you did in the above example, you’re calling the class constructor, which creates, initializes, and returns a new object by triggering Python’s internal instantiation process.

-  **.__new__(), which is responsible for creating and returning a new empty object.**

- ```Python’s instantiation process starts with a call to the class constructor, which triggers the instance creator, .__new__(), to create a new empty object. The process continues with the instance initializer, .__init__(), which takes the constructor’s arguments to initialize the newly created object.```

- lets say we have a `class` **Point** and if we call it `Point()` then class constructor creates, initializes, and returns a new instance of the class. This instance is then assigned to the point variable. look into the `constructor.py` file for example

- ```A subtle and important detail to note about .__new__() is that it can also return an instance of a class different from the class that implements the method itself. When that happens, Python doesn’t call .__init__() in the current class, because there’s no way to unambiguously know how to initialize an object of a different class.```
- **methods and functions without an explicit return statement just return `None` implicitly in Python**


### Building Flexible Object Initializers: example in `greet.py`
- regular argument: must need to provide value
- optional argument: its not must its optional

### Custom Object Creators
    to implement custom object creation we need to follow/remember this steps:
1. Create a new instance by calling super().__new__() with appropriate arguments.
2. Customize the new instance according to your specific needs.
3. Return the new instance to continue the instantiation process.

### Sub-classing Immutable Built-in Types
