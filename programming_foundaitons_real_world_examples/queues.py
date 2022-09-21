""" Queues
    There are multiple ways you can implement Queues in Python.
    1. You can implement a queue using Python's built-in list data structure
    2. You can import the queue module/class, create an object of the
        queue class, then use the methods such as 'put()' and 'get()' to
        work with the queue data structure. 
"""
import queue

q = queue.Queue()
print(q.empty())
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')
print(q.get())
print(q.get())
print(q.get())

""" creating a new queue object with a maximum size of
    two items
"""
q2 = queue.Queue(2)
print(q2.empty())
q2.put('bag1')
# Checking if q2 is full or not. 
print(q2.full())
q2.put('bag2')

print(q2.full())

# You cannot put items into a queue that's already full

