# List Comprehensions
myList = [1, 2, 3, 4, 5]
#print([2 * item for item in myList])


# List Comprehensions with filters
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
# print(filteredList)

# List comprehensions with functions
myString = 'My name is Bob Tim. I live in Boston'
# print(myString.split('.'))
# print(myString.split())


def cleanWord(word):
    return word.replace('.', '').lower()


[cleanWord(word) for word in myString.split() if len(myString)]

# Nested list comprehensions
