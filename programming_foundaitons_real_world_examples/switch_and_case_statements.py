""" Switch and case statments """

# Note 1; Python actually does not have a switch-statment structure??
# (Unlike any other programming language,
#  python language does not have switch statement functionality.)
# But Python can accomplish something similar to Java's switch-statment
# structure using a dictionary.

"""I'll have the special! """

today = 'Saturday'

if today is 'Sunday':
    print('Order the spinach pizza.')
elif today is 'Monday':
    print('Order the mushroom pizza.')
elif today is 'Tuesday':
    print('Order the pepperoni pizza.')
elif today is 'Wednesday':
    print('Order the veggie pizza.')
elif today is 'Thursday':
    print('Order the bbq chicken pizza.')
elif today is 'Friday':
    print('Order the sausage pizza.')
elif today is 'Saturday':
    print('Order the Hawaiian pizza')

specials = {'Sunday' : 'spinach',
            'Monday' : 'mushroom',
            'Tuesday': 'pepperoni',
            'Wednesday': 'veggie',
            'Thursday' : 'bbq chicken',
            'Friday' : 'sausage',
            'Saturday' : 'Hawaiian'}

def order(day):
    pizza = specials[day]
    print('Order the {} pizza.'.format(pizza))

order(today)
