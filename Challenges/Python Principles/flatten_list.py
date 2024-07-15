def flatten(my_list):
    result = []
    for row in my_list:
        result += row
    return result

    
my_list = [[1, 2], [3, 4]]
# [1, 2, 3, 4]
print(flatten(my_list))