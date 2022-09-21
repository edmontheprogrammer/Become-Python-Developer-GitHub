# Create and combine sets
# Sets:
# Store groups of like objects
# Each item unique
# No order 

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

friends = college.union(coworker, family)
