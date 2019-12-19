import random

l = ['самовар', 'весна', 'лето']

word = l[random.randint(0,len(l)-1)]
letter = random.randint(0,len(word)-1)
guess = list(word)[letter]

out = list(word)
out[letter] = '?'
print(''.join(out))

a = input('Введите букву: ')

if a:

    if a == guess:
        print('Победа!')
    else: print('Увы, попробуйте в другой раз')
    print('Слово:',word)
    
else: print('Введите букву!')
