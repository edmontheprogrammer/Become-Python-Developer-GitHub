# Control Flow

# If/ Else Statments
# a = False
# if a:
#     print('It true!')
#     print('Also print this')
# else:
#     print('It is false!')
# print('Always print this')

# a = True
# b = False
# c = True
# if a:
#     print('It true!')
#     print('Also print this')
#     if b:
#         print('Both are true')
#         if c:
#             print('All three are true')
# else:
#     print('It is false!')
# print('Always print this')

# For Loops
# a = [1, 2, 3, 4, 5]
# # Note 1: the 'in' keyword in the for-in-loop is different than the 'in' keyword in this statment: 4 in a
# # the 'in' keyword in the for-in-loop say for each item in the list do something with that item.
# # 'item' is just a variable we are declaring.
# # On the other hand, the 'in' keyword in this statment "4 in a" checks if '4' is in the 'a' which returns a Boolean
# # value 'True'.
# for item in a:
#     print(item)
# print(4 in a)  # Returns a Boolean value True.

# While loop
# Note you must have a value that terminates a while-loop
a = 0
while a < 5:
    print(a)
    a = a + 1
