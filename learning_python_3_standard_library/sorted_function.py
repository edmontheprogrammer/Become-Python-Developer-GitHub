# Built-in Function: sorted(x)
# We can sort data with the sorted function. The sorted() function takes one input, an iterable,
# Examples of Iterables are Lists, tuples, strings, dictionaries, etc
# The sorted() function then outputs a list wiht the items from the input sorted
# The sorted() function also has optional parameters that can change the order or directions of the items that will get sorted
# such as reverse or not ? Case sensitive or not?
# The sorted() function is useful because it's the easiest way to organize and sort data in our code
# Sorting elements from least to greatest


from audioop import reverse


pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# sorting elements in alphabetical order
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "jerry"]))

# sorting elements with optional key parameters
print(sorted("My favoite child is Linda".split(), key=str.upper))

# using the optional parameter 'reverse=True' to change the order from 'least to greatest' to 'greatest to least'
print(sorted(pointsInaGame, reverse=True))


leaderBoard = {231: "CKL", 123: "abc", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))


students = [('alice', 'B', 12), ('eliza', 'A', '16'), ('tae', 'C', 15)]
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
