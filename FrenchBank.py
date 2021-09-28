co = float(input("Input Capital: "))
i = float(input("Input Interest: ")) / 100
n = int(input("Input Years: "))
x = 0
paid = float(0)

while x < n :
    total = co * (i * (pow((1 + i),n))) / (pow((1 + i), n) -1)
    paid = paid + total
    print(round(total,2), "€ - ", round(paid, 2), "€")
    x += 1