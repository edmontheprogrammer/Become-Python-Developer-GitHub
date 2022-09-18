# Searching for an item in  an ordered list
# this technique uses a binary search

# Creaing a list of items
items = [6, 8, 19, 20, 23, 41, 49, 56, 87]

# Creating the binary search that takes two input parameters: 'item' and 'itemlist'


def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # TODO: if the item is found, return the index
        if itemlist[midPt] == item:
            return midPt

        # TODO: otherwise get the next midpoint
        if item > itemlist[midPt] == item:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
# 87 is outputting None error ??
print(binarysearch(87, items))

# Not 1; 250 is not on the 'items' list
print(binarysearch(250, items))
