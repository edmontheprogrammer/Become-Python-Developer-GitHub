# List
# my_list = [1, 2, 3, 4]
# print(my_list)
# my_list = ['list', 'of', 'strings']
# my_list = [1, 'list', False, []]
# my_list = [[1, 2, 3], [False, True], []]
# print((len(my_list)))

# Sets
# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# print(type(my_set))
# print(len(my_set))
# my_set = {1, 1, 2, 2}
# print(len(my_set))
# print(my_set)

# print([1, 2] == [1, 2])  # comparing lists
# print([1, 2] == [2, 1])  # comparing lists, order of elements in a list matters

# # comparing sets, returns True, the order of elements in a set does not matter
# print({1, 2, 3} == {3, 2, 1, 1, 1})

# Tuples
# my_tuple = (1, 2, 3)
# print(len(my_tuple))

# # comparing tuples, Returns False, order of elements matters in Tuples.
# print((1, 2) == (2, 1))
# # You cannot add or append elements to tuples
# my_list = [1, 2, 3, 4]
# my_list.append(6)  # You can append elements to a list
# my_tuple.append(4) # Returns Error: AttributeError: 'tuple' object has no attribute 'append'. You cannot
# # modify tuples. Once a tuple is declared, you can't add to it or change any of the values in it.
# Why Use Tuples?
# * Tuples are more efficient data structure in memory
# * Tuples are good for storing lots of little things, like x, y coordinates

# Dictionaries
my_dictionary = {
    'apple': 'A red fruit',
    'bear': 'A scary animal'
}

print(my_dictionary['apple'])
my_dictionary = {
    'apple': 'A red fruit',
    'bear': 'A scary animal',
    'apple': 'sometimes a green fruit'
}  # The keys of dictionaries must be unique
print(my_dictionary)

"""
    * Sets and Dictionaries
        * Both are defined with curly brackets 
        * Sets have uniuqe values, dictionaries have unique keys 
        * The order doesn't matter 
"""