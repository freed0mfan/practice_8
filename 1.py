best = 0
score = 0
while score != -1:
    score = int(input('Результат: '))
    if score > best:
        best = score
print(best)
