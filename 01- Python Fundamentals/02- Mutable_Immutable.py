
# * Mutable & Immutable types in Python:

# Immutables: Immutable objects cannot be modified after they are created.
# When you modify an immutable object, Python creates a new object rather than modifying the existing one.
# Examples of immutable objects include integers, floats, strings, tuples, and frozensets.

x = 5
print(id(x))  # 140718370540088 (memory location)

x = x * 2
print(id(x))  # 140718370540248 (New memory location)


# Mutables:Mutable objects can be modified after they are created.
# When you modify a mutable object, the changes are reflected in the same object.
# Examples of mutable objects include lists, dictionaries, sets, and user-defined classes.

my_list = [1, 2, 3, 4]
print(id(my_list))  # 1585863383296 (Memory location)
my_list.append(5)

print(id(my_list))  # 1585863383296 (Same Memory location)
