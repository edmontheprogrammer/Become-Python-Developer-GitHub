# Bubble sort algorithm

# creating a method named 'bubbleSort()' that takes a 'dataset' as input parameter
def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    # Creating a loop that will examin every element on the 'dataset' and perform swaps on the elements until
    # the 'dataset' is sorted.
    # The outter-loop examins every element in the 'dataset'
    # the innter-loop does all the comparisons of elements with the if-statment
    # Note 1; the nested loop (outter-loop and inner-loop) is the indicator that you have 'O( n^2)' runtime
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp

         # a print() statment that prints the dataset
        print("Current state: ", dataset)


# creating a main() method that has a list of numbers named 'list1'
# the 'main()' method calls the 'bubbleSort()' with 'list1' as the input parameter or dataset
# we are calling 'bubbleSort()' on 'list1' so that we can sort out the data or contents of 'list1'
# then a print statment that prints the contents of the 'list1' after it has been sorted
def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
