todo = {
    'task': [],
    'cat': [],
    'date': []
    }

while True:
    print('\nПростой todo:\n 1. Добавить задачу\n 2. Вывести список задач\n 3. Выход')
    do = input('Укажите число: ')

    if do.isdigit():
            do = int(do)
            if do == 3:
                break
            if do == 1:
                todo['task'].append(input('Сформулируйте задачу: '))
                todo['cat'].append(input('Добавьте категорию к задаче: '))
                todo['date'].append(input('Добавьте время к задаче: '))
            if do == 2:
                for i in range(0, len(todo['task'])):
                    print('Задача:', todo['task'][i], 'Категория:', todo['cat'][i], 'Дата:', todo['date'][i])
    else: print('Ошибка ввода')
