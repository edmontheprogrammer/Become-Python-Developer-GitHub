# Try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
# creating a queue data structure using 'deque()'
queue = deque()

# TODO: add some items to the queue
# Using the 'append()' method to add items on to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)


# TODO: print the queue contents
# Using the print method to output the contents of the queue
print(queue)

# TODO: pop an item off the fron of the queue
# Using the popleft() method to remove an item from the front of the queue
x = queue.popleft()

print("x value ", x)

print("queue = ", queue)
