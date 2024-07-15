def only_ints(x, y):
    if type(x) == int and type(y) == int:
        return True
    else:
        return False

x = 1
y = 2

print(only_ints(x, y))