# Python does not have a built-in data type or module called stack.
# Instead we can use Python's built-in data structure to accomplish the same
# thing as a stack or create the stack

# Note 1; creating a stack using Python's built-in list method
# Note 2; index 0 is the bottom of the stack
# Note 3; index stack[-1] is the top of the stack 
stack = list()

stack.append('bill1')
stack.append('bill2')
print(stack.pop())
stack.append('bill3')
stack.append('bill4')
print(stack.pop())
print(stack.pop())
print(stack.pop())
