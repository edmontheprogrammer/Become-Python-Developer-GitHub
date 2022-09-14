import time
# Errors and Exceptions
#print(1 / 0)

# Try / Except


def causeError():
    try:
        return 1/0
    except Exception as e:
        return e


# causeError()


def causeError2():
    try:
        return 1/0
    except Exception as e:
        print('There was some sort of error!')


# causeError2()

# Finally


def causeError3():
    try:
        return 1/1
    except Exception as e:
        print('There was some sort of error!')
    finally:
        print('THis will always execute!')


# causeError3()

def causeError4():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception as e:
        print('There was some sort of error!')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')


# causeError4()


# Catching Exceptions by Type

def causeError5():
    try:
        return 1 + 'a'

    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception as e:
        print('There was some sort of error!')


causeError5()


# Custom Decorators

def handleExceptionA(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception as e:
            print('There was some sort of error!')
    return wrapper()


@handleExceptionA
def causeErrorA():
    return 1/0

# Raising Exceptions


@handleExceptionA
def raiseErrorB(n):
    if n == 0:
        raise Exception()
    print(n)



# Note: Exception is a class. It has attributes.
