
import json
from json import JSONDecodeError

# JSON

# Loading JSON
# Remember that JSON is not Python
jasonString = '{"a": "apple", "b": "bear", "c": "cat"}'

try:
    json.load(jasonString)
except json.JSONDecodeError:
    print('Could not parse JSON')

# Dumping JSON

pythonDict = {"a": "apple", "b": "bear", "c": "cat"}
json.dump(pythonDict)

# Custom JOSON Decorders
