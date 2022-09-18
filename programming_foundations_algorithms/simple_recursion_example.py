# Use recursion to implement a countdown counter

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        print("Foo")


# calling the countdown() method with the input '5'
countdown(5)
