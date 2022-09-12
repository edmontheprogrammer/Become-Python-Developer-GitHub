# user_text = input('Enter some text')

# print(user_text.upper())

# user_number = input("What do you want to double? ")

# print(int(user_number) * 2)

text = input('Please enter some text')
text_version_choice = input('Enter 1 to upper case 2 to lowercase')

if int(text_version_choice) == 1:
    print(text.upper())
if int(text_version_choice) == 2:
    print(text.lower())
