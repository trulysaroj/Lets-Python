
# Class: Blueprint for creating objects
# Object: Instance of classes


# Class: Car
# Object: Tesla, Range Rover, ferrari


# Example:
class Point:
    def draw(self):
        print('Drawing Point ...')


# creating object:
point = Point()

# checking is instance or not:
print(isinstance(point, Point))  # True
print(isinstance(point, str))  # False
