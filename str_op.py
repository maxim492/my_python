x = 'У лукоморья 123 дуб зеленый 123'

if x.index('я') != -1:
    print('Позиция "я" в строке: ',x.index('я'))
else: print('В строке нет "я"')


print('Буква "у" встречается',x.count('у'),'раз(а)')

if x.isalpha() == False:
    print(x.upper())

if len(x) > 4:
    print(x.lower())

print(s.replace(s[0],'О'))
