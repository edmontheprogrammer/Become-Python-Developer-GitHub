# Implementing default values in data classes

from dataclasses import dataclass,  field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # You can define default values when attributes are declared
    # Note 1; When assigning default values to attributes, the 'attributes without'
    # default values must come first.
    title: str = "No Title"  # "No Title" is the default value here
    author: str = "No Author"  # "No Author" is the default value here
    pages: int = 0  # '0' is the default value here
    # price: float = 0.0  # '0.0' is the default value here
    # '0.0' is the default value here
    price: float = field(default_factory=price_func)


b1 = Book()
print(b1)  # Note that all the default values get printed here
# Outputs: Book(title='No Title', author='No Author', pages=0, price=0.0)
