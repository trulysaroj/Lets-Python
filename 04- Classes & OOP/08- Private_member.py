
# Private membeer - for hiding peoperties

# Creating custom containers in class using built in data types:
class TagBox:
    # private member (__)
    def __init__(self):
        self.__tags = {}

    # add methods
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # magic method for getting item
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # magic method for getting size of conrtainer
    def __len__(self):
        return len(self.__tags)

    # magic method for iterating object properties
    def __iter__(self):
        return iter(self.__tags)


# creating object
box = TagBox()

box.add('django')
box.add('Django')
box.add('django')

print(box.__tags) #'TagBox' object has no attribute '__tags'
