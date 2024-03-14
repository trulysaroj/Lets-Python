# Inheritence in python

# Animal class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


# Inheritating properties of animal in Mammal & Fish

# Animal Class: Parent, Base
# Mammal class: Child, sub-class
class Mammal(Animal):

    def walk(self):
        print("Walk")


# Animal Class: Parent, Base
# Fish class: Child, sub-class
class Fish(Animal):

    def swim(self):
        print("swim")


# creating both Mammas & fish object
human = Mammal()
tuna = Fish()

human.eat()  # Eat
tuna.eat()  # Eat

print(human.age)  # 1
print(tuna.age)  # 1

# checking if it instance or not
print(isinstance(human, Mammal))  # True
print(isinstance(human, Animal))  # True
# * Object class is the base class of all class ------
print(isinstance(human, object))  # True

# checking if it is subclass or not
print(issubclass(Fish, Animal))  # True
print(issubclass(Mammal, Animal))  # True
print(issubclass(Mammal, object))  # True


# * Note: Avoid Multi-level inheritence as much as possible


# GOOD EXAMPLE of Inheritence use propely:

# class for custom error
class InvalidOperatioError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opended = False

    def open(self):
        if self.opended:
            raise InvalidOperatioError("Stream is already opened ...")
        self.opended = True

    def close(self):
        if not self.opended:
            raise InvalidOperatioError("Stream is already closed ...")
        self.opended = False


# Inheritasting Stream class
class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")
