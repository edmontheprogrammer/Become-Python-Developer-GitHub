""" Add items to dictionaries """

# dictionary of name/number pairs
# Note 1; Dictionaries are similar to sets, they do not allow additions of
# duplicate keys. If you try adding a second item with the same key,
# Python will overwrite the existing key with the new one. 
rolodex = {'Aaron': 5556069,
           'Bill' : 5559824,
           'Dad'  : 5552603,
           'David': 5558331,
           'Dillon' : 5553538,
           'Jim' : 5555547,
           'Mom' : 5552603,
           'Olivia' : 5556397,
           'Verne' : 5555309}

rolodex['Amanda'] = 5559754

print(rolodex['Amanda'])

print(rolodex['David'])

rolodex['David'] = 5550902

print(rolodex['David'])

# you can add a tuple as a value to dictionary if you want to store
# multiple phone numbers
rolodex['David'] = (5558331, 5550902)
print(rolodex)
print(rolodex['David'])

rolodex['David'] = 5558331
rolodex['David (Amanda)'] = 5550902
print(rolodex['David'])
print(rolodex['David (Amanda)'])
