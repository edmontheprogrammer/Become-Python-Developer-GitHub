# Files

# Reading Files

f = open('file1.text', 'r')
# print(f)  # Outputs a file object

# print(f.readline())  # This reads contents  of the file one line at a time

# print(f.readlines())  # this all contents of the file all at once.

# printing contents of the file using a for-loop
for line in f.readlines():
    print(line.strip())

# Writing Files

f = open('Output_file2.text', 'w')
print(f)  # Outputs a file object
f.write('Line 1\n')
f.write('Line 2\n')
f.close()

# Appending Files
f = open('Output_file2.text', 'a')
print(f)  # Outputs a file object
f.write('Line 3\n')
f.write('Line 4\n')
f.close()  # It's very imporant to call the close() method.
with open('Output_file2.text', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')


print(f)
