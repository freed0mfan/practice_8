n = int(input('N: '))
perfect = 0
for i in range(2, n + 1):
    dividers_sum = 0
    for d in range(1, i):
        if i % d == 0:
            dividers_sum += d
    if i == dividers_sum:
        perfect += 1
print(perfect)
