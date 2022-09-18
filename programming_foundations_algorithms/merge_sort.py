# Implement a merge sort with recursion

# Creating a list of items
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

# Creating a method named 'mergesort()' that takes 'dataset' as input


def mergesort(dataset):
    # Creating an if-statment that checks if the size of the 'dataset' is greater than one,
    # then split the the 'dataset' into two lists: "lefatrr" and "rightattr"
    # This operation will continue as long as the 'dataset' length is greater than one.
    # "if len(dataset) > 1" is the breaking condition
    if len(dataset) > 1:
        mid = len(dataset) // 2
        lefttarr = dataset[:mid]
        rightatrr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(lefttarr)
        mergesort(rightatrr)

        # TODO: now perform the merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into merged array

        # TODO: while both array have content
        while i < len(lefttarr) and j < len(rightatrr):
            if lefttarr[i] < rightatrr[j]:
                dataset[k] = lefttarr[i]
                i += 1
            else:
                dataset[k] = rightatrr[j]
                j += 1
            k += 1

        # TODO: if the left array still have values, add them
        while i < len(lefttarr):
            dataset[k] = lefttarr[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightatrr):
            dataset[k] = rightatrr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
