# Tuples and Sets
# Sets
# mySet = {'a', 'b', 'c'}
# # print(mySet)
# mySet = set(('a', 'b', 'c'))
# print(mySet)

# myList = ['a', 'b', 'c', 'c']
# myList = list(set(myList))
# print(myList)

# Tuples
# Tuples are more efficent than lists
# They don't grow or change
myTuple = ('a', 'b', 'c')
print(myTuple)


def returnsMultipleValues():
    return (1, 2, 3)


print(type(returnsMultipleValues()))

a, b, c = returnsMultipleValues()
print(a)
print(b)
print(c)
