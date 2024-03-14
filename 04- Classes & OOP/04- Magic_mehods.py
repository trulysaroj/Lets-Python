
# magic methods -
# special methods in Python that start and end with double underscores.
# These methods allow classes to emulate built-in behavior and syntax within Python

# some examples

# Class and instances methods:

class Point:

    # __init__ magic mthods
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # __str__ magic methos:
        def __str__(self):
            return f"({self.a}, {self.b})"

    # Class methods:
    @classmethod
    def default(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Your drawing point is at {self.a}, {self.b}")


# creating instance
point = Point(2, 5)
print(point)  # (2, 5)

print(str(point))
