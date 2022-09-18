# determine if a list is sorted

# Creating two lists for us to operate on. These are the lists that will get pass into the 'is_sorted()'
# so it can determine if the list is sorted or not
# 'item1' is sorted in order, but 'item2' is NOT sored
items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 48, 43]

# creating the 'is_sorted()' method which takes 'itemlist' as input parameter


def is_sorted(itemlist):
    # TODO: using the brute force method
    for i in range(0, len(itemlist) - 1):
        if (itemlist[i] > itemlist[i + 1]):
            return False

    # note 1; the 'all()' function is a boolean method that return either True or False
    return all(itemlist[i] <= itemlist[i + 1] for i in range(len(itemlist) - 1))

    # return True


# calling the 'is_sorted()' method and passing in list as input parameter
print(is_sorted(items1))  # Outputs 'True' because 'item1' is sorted in order
print(is_sorted(items2))  # Outputs 'False' because 'item2' is NOT sorted
