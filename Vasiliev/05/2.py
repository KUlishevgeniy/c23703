# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

a = ['Ivan', 'NeIvan', 'Kb', 'Mp', 'Genius', 'students', 'others']

print('На районе живут ', end='')
print(*a, sep=', ')