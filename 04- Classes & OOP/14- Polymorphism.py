
#  polymorphism in python:

class Animal:
    def sound(self):
        pass


class Dog:
    def sound(self):
        return 'woof ..'


class Cat:
    def sound(self):
        return 'Meow ..'

# Function that accepts any Animal and makes it produce sound


def make_sound(animal):
    print(animal.sound())


# creating instace of dog and cat:
dog = Dog()
cat = Cat()


# Calling the function with different types of animals
print(make_sound(dog))  # woof ..
print(make_sound(cat))  # Meow ...
