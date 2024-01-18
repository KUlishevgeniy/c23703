# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches(start_point, angle, length):
    sd.line(root_point, root)
    v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length, width=1)
    v1.draw()
    next_point1 = v1.end_point
    next_angle1 = angle + (sd.random_number(26, 46))
    v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length, width=1)
    v2.draw()
    next_point2 = v2.end_point
    next_angle2 = angle - (sd.random_number(26, 30))
    next_length = length * (sd.random_number(65, 85) / 100)
    if length < 8:
        return
    else:
        draw_branches(next_point1, angle=next_angle1, length=next_length)
        draw_branches(next_point2, angle=next_angle2, length=next_length)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
root_point = sd.get_point(300, 30)
root = sd.get_point(300, 0)
 
draw_branches(start_point=root_point, angle=90, length=200)

# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


