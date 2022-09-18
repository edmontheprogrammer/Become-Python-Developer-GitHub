# Demonstrate hashtable usage

# TODO: create a hashtable all at once
item1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(item1)

# TODO: create a hashtable progressively
item2 = {}
item2["key1"] = 1
item2["key2"] = 2
item2["key3"] = 3
print(item2)

# TODO: try to accessa nonexistent key
# Results in a KeyError because there's no data value associated with the key 'key6'
# print(item1["key6"])

# TODO: replace an item
item2["key2"] = "two"

print(item2)

# TODO: iterate the keys and values in the dictionary using the built-in item function in Python
for key, value in item2.items():
    print("Key: ", key, " value: ", value)
