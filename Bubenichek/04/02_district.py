# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

na_rayone = [15335, 19, -65, 'sheep', 'vladimir alexeevich', 'маша', 'VOID', False, -43.009, {'ice cream': 'good'}]

print('На районе живут ', end='')
print(*na_rayone, sep=', ')




