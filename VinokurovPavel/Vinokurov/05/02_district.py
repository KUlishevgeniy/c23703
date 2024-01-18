# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1 import room1 as c11, room2 as c12
from district.central_street.house2 import room1 as c21, room2 as c22
from district.soviet_street.house1 import room1 as s11, room2 as s12
from district.soviet_street.house2 import room1 as s21, room2 as s22

villages = [c11.folks, c12.folks, c21.folks, c22.folks,
s11.folks, s12.folks, s21.folks, s22.folks]

folks_s = []

for i in villages:
    for k in i:
        folks_s.append(k)


print('На районе живут: ' + ', '.join(folks_s))


