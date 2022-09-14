# Function Scope
# Creating a funciton named 'performOperation' that takes in two
# input parameters, arguments, and keyword arguments
# the function prints boths 'args' and 'kwargs'
from threading import local


# def performOperation(*args, **kwargs):
#     print(args)
#     print(kwargs)


# # calling the performOperation
# performOperation(1, 2, operation='sum')

# locals()
def performOperation(num1, num2, operation='sum'):
    print(locals())


# calling the performOperations
# Note locals() is a built-in method in Python
performOperation(1, 2, operation='multiply')

# globals()
print(globals())

message = 'Some golbal data'
varA = 2

# Global and Local Scope.


def function1(varA, varB):
    message = 'Some local data'
    print(varA)
    print(message)
    print(locals())


def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())


function1(1, 2)
function2(3, 4)

# Python allows you to define a function within another function
# Note that we cannot call the 'inner_function()' outside of the outter function or the function where the inner funciton is
# defined in.


def function1(varA, varB):
    message = 'Some local data'
    print(varA)

    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')

    print(locals())
    inner_function(123, 456)


function1(1, 2)
# inner_function(123, 456) syntax error because inner function is not defined in this scope.
