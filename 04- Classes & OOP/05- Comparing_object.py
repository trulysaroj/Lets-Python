
# Comparing two objects

class Point:
    # __init__ magic mthods
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # __ep__ methods for comparing two objects equality
    def __eq__(self, point2):
        return point.a == point2.a and point.b == point2.b

    # __gt__ methods for comparing grater than value

    def __gt__(self, point3):
        return self.a > point3.a and self.b > point3.b

    def draw(self):
        print(f"Your drawing point is at {self.a}, {self.b}")


# instances
point = Point(3, 5)
point2 = Point(3, 5)

# False -- cuz both object are stored in two different memory locations
print(point == point2)


# For comparing a object with __eq__ mthods
print(point == point2)  # True


# comparing greater value wiht __gt__
point3 = Point(20, 50)
print(point3 > point2)  # True
print(point3 < point2)  # False
