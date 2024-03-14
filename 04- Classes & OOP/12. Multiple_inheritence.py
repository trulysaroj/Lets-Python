
#  Multiple inheritence example:

class Employee:
    def greet(self):
        print("greeting from Employee ...")


class People:
    def greet(self):
        print("greeting from People ...")


# Multiple inheritence:
class Manager(Employee, People):
    pass


# creating object with Manager class
manager = Manager()
print(manager.greet())
# greeting from Employee ... (first order methods will be assigned)


# * Note: Sometimes Multiple inheritence is also not good if not used properly


# GOOD EXAMPLE of Multiple Inheritence:
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


# inheritating both class:
class FlyingFish(Flyer, Swimmer):
    pass
