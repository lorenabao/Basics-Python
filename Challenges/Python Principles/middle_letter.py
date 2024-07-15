def mid(string):
    position = int(len(string)/2)
    if len(string) % 2 == 0:
        return ""
    else:
        return string[position]

string = "acd"
print(mid(string))