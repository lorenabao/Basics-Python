# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

# What makes this tricky is that your function body must only contain a single line of code.
def convert(lst):
    return [str(element) for element in lst]
numbers = [1, 2, 3]
print(convert(numbers))

# using map
def convert(ns):
    return list(map(str, ns))