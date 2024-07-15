# row 1:      X | O | X
#           -----------
# row 2:        |   |  
#           -----------
# row 3:      O |   |
#       column column column
#             A    B    C

# Get content
# def get_row_col(element):
    
#     board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]
#     column = element[0]
#     row = int(element[1:])

#     if column == "A":
#         column = 0
#     elif column == "B":
#         column = 1
#     else:
#         column = 2
#     return board[row][column]


def get_row_col(element):
    
    board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
    column = element[0]
    row = int(element[1])-1


    if column == "A":
        return (row, 0)
    elif column == "B":
        return (row, 1)
    else:
        return (row, 2)
    
element = "A1"


print(get_row_col(element))

# Other response
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)