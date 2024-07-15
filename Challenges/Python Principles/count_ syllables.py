# Define a function named count that takes a single parameter. 
# The parameter is a string. 
# The string will contain a single word divided into syllables by hyphens, such as these:

def count(string):
    return len(string.split('-'))

string = "ho-tel"

print(count(string))