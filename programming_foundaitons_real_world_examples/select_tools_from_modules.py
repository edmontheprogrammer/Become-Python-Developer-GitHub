""" importing an entire module"""
import random

""" accessing a specific method rom the
    the random module
"""
print(random.randint(1, 20))

""" importing a specific method from a
    module
"""
from random import randint
print(randint(1, 20))

print(random.random())

""" giving the random module a different
    name to avoid naming conflicts 
"""
import random as rand

print(rand.randint(1, 20))
