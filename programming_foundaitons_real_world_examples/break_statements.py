""" Break statement """

import random

# 20 clean dishes in dishwasher
dishwasher = ['plate', 'bowl', 'cup', 'fork', 'spoon', 'cup', 'plate']

for dish in list(dishwasher):

    # check space left in cabinet
    if not random.randint(0, 19):
        print('Out of space!')
        break
    else:
        print('Putting {} in the cabinet'.format(dish))
        dishwasher.remove(dish)
