euro = 1
turkish_lira = 36.70


amount = input("Type amount: ")

currency = input("Convert to Euro or Lira?: ")

if currency == "Euro":
    result = int(amount) * euro / 100
else:
    result = int(amount) *turkish_lira /100

print(result)
    

