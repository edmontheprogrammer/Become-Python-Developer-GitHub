""" For loops """


""" Loading the Dishwasher """

# dirty dishes in the sink

# Creating a list called sink that has three dirty dishes 
sink = ['bowl', 'plate', 'cup']

# Creating a for-loop that loops over items in the sink list.
# 
for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)
