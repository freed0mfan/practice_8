income = ''
s = 0
n = 0
while income != 0:
    income = int(input('доход: '))
    n += 1
    s += income
print(s / (n - 1))
