# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# v1 = sd.get_vector(start_point=point, angle=0, length=100, width=2)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=100, width=2)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=100, width=2)
# v3.draw()

# нарисовать треугольник из точки (200, 200) с длиной стороны 100
length = 100
point = sd.get_point(200, 200)
def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=2)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=100, width=2)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=100, width=2)
    v3.draw()


point_0 = sd.get_point(200, 200)

for angle in range(0, 361, 120):
    triangle(point=point_0, angle=angle)





# нарисовать квадрат из точки (200, 200) с длиной стороны 100
length = 100
point = sd.get_point(200, 200)


# определить функцию рисования квадрата из заданной точки с заданным наклоном
def square(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=2)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=200, width=2)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=200, width=2)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=200, width=2)
    v3.draw()



point_0 = sd.get_point(200, 200)

for angle in range(0, 361, 90):
    square(point=point_0, angle=angle)



# нарисовать пятиугольник из точки (200, 200) с длиной стороны 100
length = 100
point = sd.get_point(200, 200)


# определить функцию рисования квадрата из заданной точки с заданным наклоном
def pentagon(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=200, width=2)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=200, width=2)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=200, width=2)
    v3.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=200, width=2)
    v3.draw()
    
   

point_0 = sd.get_point(200, 200)

for angle in range(0, 361, 72):
    pentagon(point=point_0, angle=angle)






# нарисовать шестиугольник из точки (200, 200) с длиной стороны 100
length = 100
point = sd.get_point(200, 200)


# определить функцию рисования квадрата из заданной точки с заданным наклоном
def hexagon(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=200, width=2)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=200, width=2)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=200, width=2)
    v3.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=200, width=2)
    v3.draw()
    
    v6 = sd.get_vector(start_point=v4.end_point, angle=angle + 300, length=200, width=2)
    v3.draw()



point_0 = sd.get_point(200, 200)

for angle in range(0, 361, 60):
    hexagon(point=point_0, angle=angle)




# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
