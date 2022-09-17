
# creating a variable named 'primaryColors' and assigning it to a 'set()' method.
# 'set()' is a built-in function that can take a list and convert it to a
# set data type. Here we passing a list of strings and convert it to a set.
# primaryColors = set(["red", "blue", "yellow"])
# 'frozenset' is a method that makes 'set' finite, meaning we cannot add items to it??
# In Python, we can add items to a 'set' as long as the 'set' is not a 'frozenset'
primaryColors = frozenset(["red", "blue", "yellow"])

# creating a string varibale named 'color' and assigning it to the string literal "green"
color = "green"

# a simple if-else statment that checks if the 'color' is in the 'primaryColors' set
# then it prints the 'color' value and a string
if color.lower() in primaryColors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

letters = set(['a', 'b'])
letters.add('c')
print(letters)
