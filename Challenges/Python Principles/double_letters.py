def double_letters(string):
    for index in range(len(string)-1):
        if string[index] == string[index+1]: 
            return True
        else:
            index+1 
    else:
        return False

string = "abc"
print(double_letters(string))