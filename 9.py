n = int(input('N: '))
k = 2


def prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


while k <= n:
    if prime(k):
        print(k)
    k += 1
