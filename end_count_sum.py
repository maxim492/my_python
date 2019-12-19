summ = 0

while True:
    a = input('Введите число или Стоп для выхода: ')
    if a.lower() == 'стоп':
        break
    if a.isdigit():
        summ += int(a)
    else: print('Ошибка ввода')
print('Сумма:', summ)
