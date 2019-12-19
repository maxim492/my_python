def f(st,num):
    if len(st) > num:
        return st.upper()
    else: return st

s = input('Введите строку:\n')
n = input('Введите число: ')

if s:
    if n:
        print(f(s,int(n)))
    else: print('Введите число!')
else: print('Введите строку!')
