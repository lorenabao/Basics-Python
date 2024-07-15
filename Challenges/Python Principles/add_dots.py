def add_dots(string):
    return ".".join(string)

def remove_dots(string):
    return string.replace(".", "")

string = "test"
print(add_dots(string))
print(remove_dots(add_dots(string)))