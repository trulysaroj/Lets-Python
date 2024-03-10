
# * Simple Queues Data Structure Implementation in python
# FIFO Method ---> First in Fist out

# Importing deques object
from collections import deque

customer_queue = deque([])

# adding items on queue
customer_queue.append('person1')
customer_queue.append('person2')
customer_queue.append('person3')
customer_queue.append('person4')

print(customer_queue)  # deque(['person1', 'person2', 'person3', 'person4'])


# removing items from the begininng of the queue
customer_queue.popleft()
customer_queue.popleft()
customer_queue.popleft()

print(customer_queue)  # deque(['person4'])

# chekcing if queues becomes empty:
if not customer_queue:
    print('Hurry, this queues becomes empty ...')
