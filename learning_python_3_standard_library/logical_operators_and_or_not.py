# Note 1; What is a boolean?
# a boolean is a variable that has two possible values: 'True' or 'False'

# What is a Boolean?
# these are two boolean values.
isRaining = False
isSunny = True


# Logical Operators:
# Logical operators takes one or more boolean values and operates on them
# 'and' 'or' 'not' are the main logical operators we will be working on

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

if isRaining and isSunny:
    print(" We might see a rainbow")


# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false

if isRaining or isSunny:
    print("It might be rainy or it might be sunny")

# NOT
# true --> false
# false --> true

if not isRaining:
    print("It must be raining")

ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult.")
