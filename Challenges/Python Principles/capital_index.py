def capital_indexes(string):
    return [i for i, char in enumerate(string) if char.isupper()]

string = "HHHEODkcnkjpefup23WDWW"

print(capital_indexes(string))