# Variables as Functions
x = 5


def x():
    return 5


print(x.__code__.co_varnames)
print(x.__code__.co_code)
# Viewing function data with __code__

# Text processing in Python
'''
    This is a 
    mutil-line 
    texts
'''
