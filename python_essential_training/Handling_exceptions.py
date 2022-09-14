# Handling Exceptions
# Try / Except

def causeError():
    try:
        return 1/0
    except Exception as e:
        return e


print(causeError())

# Finally

# Catching Exceptions by Type

# Custom Decorators

# Raising Exceptions
