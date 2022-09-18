# Try out the Python stack functions

# 1TODO: create a new empty stack
# creating a Stack data structure using the Python list
stack = []

# 1TODO: push items onto the stack
# Using the built-in 'append()' method to add items onto the stack (list)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# 1TODO: print the stack contents
# using the print() method to output the contents of the stack (list) which outputs [1, 2, 3, 4]
print(stack)

# 1TODO: pop an item off the stack
# Using the built-in 'pop()' method to pop an item off the stack (list)
# The item that gets removed from the stack is stored in 'x'
x = stack.pop()  # 'x' now contains value '4'

print(stack)  # The new contents of the stack now is [1, 2, 3]
