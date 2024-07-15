def is_anagram(string):
    if string == string[::-1]:
        return True
    else:
        return False
string = "baab"
#print(is_anagram(string))

# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.

def is_anagram(x, y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False
    
x = "typhoon"
y = "opython"


# Shorter solution

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_anagram(x, y))
