

# * Simple Stack Data structure implementation:
# LIFO Methods ---> Last in first out

book_stack = []

# adding book
book_stack.append('book1')
book_stack.append('book2')
book_stack.append('book3')
book_stack.append('book4')

print(book_stack)  # ['book1', 'book2', 'book3', 'book4']

# picking book from stack
book_stack.pop()
book_stack.pop()
print(book_stack)  # ['book1', 'book2']

# getting fist book from the book stack
first_book = book_stack[-1]
print(first_book)  # book2


# when stack becomes clears
if not book_stack:
    print('Oops, your book stack is empty ...')
