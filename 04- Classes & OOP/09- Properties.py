
# Setting and getting peoperties

class Product:

    def __init__(self, price):
        self.price = price

    # with property decorator
    @property
    def price(self):
        return self.__price

    # for setting price with decorator
    @price.setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price canot be a negative")
        self.__price = value


# creating ojb from class
product = Product(60)
print(product.price)
