from collections import defaultdict

animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}

# print(animals)

# print(animals['a'])

animals['d'] = 'dog'
# print(animals)

animals['a'] = 'antelope'

# print(animals.keys())
# print(animals.values())
# print(list(animals.keys()))

# print(animals['e'])
# print(animals.get('e', 'elephant'))

# print(len(animals))

# This is a dictionary that has list as values
animals = {
    'a': ['aardvark'],
    'b': ['bear'],
}

animals['b'].append('biscon')
animals['c'] = ['cat']

if 'c' not in animals:
    animals['c'] = []

animals['c'].append('cat')

# The Default Dict

animals = defaultdict(list)

defaultdict(list, {})
animals['e'].append('e', ['elephant'])
