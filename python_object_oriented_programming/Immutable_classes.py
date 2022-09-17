# Immutable Classes

from dataclasses import dataclass



# 1TODO: The 'frozen' parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# 1TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another Value"
# print(obj.value1)

# 1TODO: even functions within the class can't change anything.
obj.somefunc(20)
