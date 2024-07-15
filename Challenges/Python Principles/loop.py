

def filtered(name):
    return [i for i, char in enumerate(name) if char == "a"]


my_list = range(1,30)
filtered_list = [i for i in my_list if i % 2]

print(filtered("Banana"))
print(filtered_list)