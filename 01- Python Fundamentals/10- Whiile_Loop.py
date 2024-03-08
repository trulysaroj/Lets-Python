

# While Loop in Python:

# Syntax:
# while condition:
# code block to be executed as long as the condition is true


# example
num = 1
while num <= 5:
    print(num)  # 1 2 3 4 5
    num += 1


# another example
total = 0
count = 1

while count <= 20:
    total += count
    count += 1
print(f"sum of numers from 1 - 20 is: {total}")


# infinte loop
# while True:
# print('This is an Infinte loop...')
