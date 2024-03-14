
# Constructors - for crating methods and values

class Point:
    # class -level attributes
    default_color = 'yellow'

    # constructor / magic methods
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method
    def draw(self):
        print(f"Your drawing is on point: {self.x}, {self.y}")


# creating object from class
point = Point(10, 20)
print(point.x)  # 10
print(point.y)  #
print(point.default_color)  # yellow


print(point.draw())  # Your drawing is on point: 10, 20


# another object
point2 = Point(2, 7)
print(point2.draw())  # Your drawing is on point: 2, 7
print(point2.default_color)  # yellow
