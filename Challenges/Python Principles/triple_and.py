# Define a function named triple_and that takes three parameters and returns 
# True only if they are all True and False otherwise.

def triple_and(x, y, z):
    return all([x, y, z])

print(triple_and(1, 1, 1))

# Another solution
def triple_and(a, b, c):
    return a and b and c