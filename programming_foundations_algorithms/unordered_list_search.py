# Searching for an item in an unordered list
# somtimes called a linear search

# declare a list of values to operate on
# In other words, creating a list of items that we can search an item in
import re


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


# creating a 'find_item()' method that takes in an 'item' that we are going to be searching for
# and 'itemlist' that's a list data type which we'll be looking over to find our item
# creating a for-in-loop with if-statment that examins the 'itemlist' and 'item'
def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i

    return None


# Calling the 'find_item()' method with the item '87' and the list 'items'
print(find_item(87, items))  # Outputs the index or position of the item
# Calling the 'find_item()' method with the item '250' and the list 'items'
# Note 1; item '250' is not on the 'items' list, therefore, the method returns 'None'
print(find_item(250, items))
