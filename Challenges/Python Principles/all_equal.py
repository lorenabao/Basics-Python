# Define a function named all_equal that takes 
# a list and checks whether all elements in the list are the same.

def all_equal(lst):
    return all(x == lst[0] for x in lst)

elements_list = [1, 1, 1]
print(all_equal(elements_list))

# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)