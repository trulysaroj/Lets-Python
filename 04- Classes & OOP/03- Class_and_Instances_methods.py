
# Class and instances methods:

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Class methods:
    @classmethod
    def default(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Your drawing point is at {self.a}, {self.b}")


# creating instace
point = Point(10, 30)
print(point.draw())  # Your drawing point is at 10, 30

# adding new attribute to instance
point.c = 30
print(point.c)  # 30

# another instance
point2 = Point.default
print(point2.draw())  # Your drawing point is at 0, 0
