num = input('Введите число: ')
while not num.isdigit():
    num = input('Ошибка. Попробуйте еще раз. Введите число: ')
else:
    print(f'Введено целое число: {num}')
