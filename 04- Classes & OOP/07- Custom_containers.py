
# Creating custom containers in class using built in data types:
class TagBox:
    def __init__(self):
        self.tags = {}

    # add methods
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # magic method for getting item
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # magic method for getting size of conrtainer
    def __len__(self):
        return len(self.tags)

    # magic method for iterating object properties
    def __iter__(self):
        return iter(self.tags)


# creating object
box = TagBox()

box.add('django')
box.add('Django')
box.add('django')

print(box.tags)  # {'django': 3}
print(len(box.tags)) // 1
