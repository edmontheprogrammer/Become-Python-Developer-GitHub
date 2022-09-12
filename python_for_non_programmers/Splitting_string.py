
text = """ This is a big piece of text. This is not a small text. The word text appears three times"""

word_count = {0}

data = text.lower().split()
for word in data:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
