# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

a = ['Kolya', 'Vova', 'Bobik', 'Biber', 'Belyash', 'Trevor', 'Habibi']

print('На районе живут ', end='')
print(*a, sep=', ')




