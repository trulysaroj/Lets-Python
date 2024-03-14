
# arothmetic operations in class object

class Point:

    # __init__ magic mthods
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # __add__ for arithmetic operations
    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)

    # __str__ magic methos:
    def __str__(self):
        return f"({self.a}, {self.b})"

    def draw(self):
        print(f"Your drawing point is at {self.a}, {self.b}")


# instances
point = Point(3, 5)
other = Point(2, 8)

combined = point + other

print(combined.a)  # 5
