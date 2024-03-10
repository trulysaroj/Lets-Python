
# * Sets
# a set is an unordered collection of unique elements. Sets are mutable, meaning you can modify them after creation.
# However, the elements within a set must be immutable,
# meaning you cannot use mutable types like lists or dictionaries as elements of a set.


# Creating set
my_set = {1, 2, 4}

# with set constructor:
numbers = [2, 1, 3, 2, 3, 2, 1, 4]
uniques_list = set(numbers)
print(uniques_list)  # {1, 2, 3, 4}


# some basic operations:
uniques_list.add(5)  # { 1, 2, 3, 4, 5}
uniques_list.remove(3)  # {1, 2, 4, 5}
print(5 in uniques_list)  # True

print(uniques_list)  # {1, 2, 3, 4}


# Some mathmetaical operations:
set1 = {1, 2, 5, 4}
set2 = {1, 4, 6, 3, 2}

print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1 & set2)  # {1, 2, 4}
print(set1 - set2)  # {5}
print(set1 ^ set2)  # {3, 5, 6}
