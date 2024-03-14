
# Methods overriding in example

# Animal class
class Animal:
    def __init__(self):
        print("Animal constructor ...")
        self.age = 1

    def eat(self):
        print("Eat")


# Inheritating properties of animal in Mammal & Fish
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor ...")
        self.weight = 65

    def walk(self):
        print("Walk")


class Fish(Animal):

    def swim(self):
        print("swim")


# creating both Mammas & fish objectd
human = Mammal()
tuna = Fish()

print(human.weight)  # 65
# print(tuna.weight)  # 'Fish' object has no attribute 'weight'
print(tuna.age)  # 1
print(human.age)  # 1
