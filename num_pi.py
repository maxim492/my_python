def pii(x):
    from math import pi
    return f'{pi:.{x}f}'

a = input('Знаки после запятой: ')

if a:
    print(pii(a))
else: print('Введите кол-во знаков после запятой!')
