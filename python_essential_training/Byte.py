# Python Byte Object
# Common behind the scenes
# used as data that gets passed in a program
# Rarely manipulated or modified directly
# The Byte object is commonly used for streaming files and transmitting text without knowing the encoding
# often used "under the hood" in Python libraries

# Creates an empty bytes object. That's 4 bytes long '\x00\x00\x00\x00'
print(bytes(4))

smileyBytes = bytes('🙄', 'utf-8')
print(smileyBytes)
print(smileyBytes.decode('utf-8'))

print(bytearray)
