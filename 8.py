num = ''
for i in range(1, 10):
    num += str(i)
    print(f'{num} * 8 + {i} = {int(num) * 8 + i}')

num = ''
for i in range(1, 10):
    num += str(i)
    print(f'{num} * 9 + {i + 1} = {int(num) * 9 + i + 1}')

num = ''
for i in range(1, 10):
    num = '1' * i
    print(f'{num} * {num} = {(int(num)) ** 2}')
