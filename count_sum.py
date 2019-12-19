a = input('Введите число: ')
sumk = 0

if a.isdigit():
    for i in list(a):
        if int(i) % 2 == 1:
            sumk += int(i)*int(i)
    print('Сумма квадратов нечетных цифр в числе:', sumk)
else: print('Введите число!')
