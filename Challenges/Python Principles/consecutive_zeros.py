# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
# Your code should find the biggest number of consecutive zeros in the string. 
# For example, given the string:
# "1001101000110"
# The biggest number of consecutive zeros is 3.

def consecutive_zeros(string):
    result = 0
    streak = 0
    for element in string:
        if element == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

number = "100000001101000110"
print(consecutive_zeros(number))


# shorter solution
def consecutive_zeros(string):
    return max([len(zero) for zero in string.split("1")])

print(number.split("1"))