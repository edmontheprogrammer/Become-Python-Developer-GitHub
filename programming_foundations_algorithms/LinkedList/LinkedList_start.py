# Linked List example

# 'Node' class repersents the 'Node' that will be stored in the LinkedList
# It's just a simple class that stores data field called 'val'
class Node(object):
    # Creating the init() method and two attributes that repersents the 'value'
    # stored in the LinkeList 'Node' and a 'pointer' named 'next' that can points to
    # the 'next'. The '__init__()' method is basically the 'head Node' when starting
    # creating a new LinkedList
    def __init__(self, val):
        self.val = val
        self.next = None

    # creating a method 'get_data()' that gives us the value stored in the 'Node'
    def get_data(self):
        return self.val

    # creating a method 'set_data' that allows us to change the value stored in the
    # current node. 'set_data' takes an input parameter named 'val' that repersents
    def set_data(self, val):
        self.val = val

    # creating a method 'get_next' that accepts an input parameter 'next'??
    def get_next(self, next):
        self.next = next


# The LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    # creating a method that returns the number of Nodes in the Linkedlist
    def get_count(self):
        return self.count

    # creating a method that inserts a new node in the linkedlist
    def insert(self, data):
        # 1TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    # creating a method that finds data from a Node in the linkedlist
    def find(self, val):
        # 1TODO: find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item.get_next()

        return None

    # Creating a method that deletes an item at a given index
    def deleteAt(self, idx):
        # 1TODO: delete an item at given index
        if idx > self.count - 1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIndx = 0
            node = self.head
            while tempIndx < idx - 1:
                node = node.get_next()
                tempIndx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    # Creating a method that prints the contents of the linked list

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
# inserting items to the linkedlist
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
# printing the contents of the linked list
itemlist.dump_list()

# exercise the list

# counts the numbers of items in the linked list
# print("Item count: ", itemlist.get_count())

# find a specific item '13' from the linkedlist
# print("Finding item: ", itemlist.find(13))

# Finding another item '78' from the linkedlist
# print("Finding item: ", itemlist.find(78))

# delee an item from the linked list
itemlist.deleteAt(3)

# get the numbers of items in the linked list after the delete operation
print("Item count: ", itemlist.get_count())

# Find another item '38' from the linked list
print("Finding item: ", itemlist.find(38))

# itemlist.dump_list()
