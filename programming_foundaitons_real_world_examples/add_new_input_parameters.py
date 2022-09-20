""" A Functional Breakfast """


def mix_and_cook():

    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")


def make_omelette(ingredients):
    mix_and_cook()
    omlette = 'a {} tasty omelette'.format(ingredients)
    return omlette


def make_pancake():
    mix_and_cook()

    pancake = "a delicious pancake"
    return pancake

"""
    The Single Asterisk (*) tells Python to expect any number of arguments when the
    function is called.
    Like a list made of arguments
"""
def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omlette with {} ingredients'.format(len(ingredients))
    return omelette 
