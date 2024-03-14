
# Duck Typing
# programming style that focuses on the behavior of an object rather than its type

# examples:

class Duck:
    def quack(self):
        print('quack ...')


class Person:
    def quack(self):
        print('I am quacking like a duck ...')


def make_it_quack(obj):
    obj.quack()


# instances
duck = Duck()
person = Person()


make_it_quack(duck)  # quack ...
make_it_quack(person)  # I am quacking like a duck ...
