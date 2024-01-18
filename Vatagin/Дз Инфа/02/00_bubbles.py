# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1800, 1000)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point= sd.get_point(100,300)
radius = 50
for i in range(3):
    radius += 5
    sd.circle(center_position = point, radius = radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def ris(point, step):
    point = sd.get_point(400, 300)
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position = point, radius = radius)
point = sd.get_point(600,300)
ris(point = point, step = 20)

# Нарисовать 10 пузырьков в ряд
X = 600
for i in range(10):
    point = sd.get_point(X, 300)
    sd.circle(center_position = point)
    X += 100

# Нарисовать три ряда по 10 пузырьков
X = 600
Y = 500
for i in range(3):
    point = sd.get_point(X, Y)
    for k in range(10):
        point = sd.get_point(X, Y)
        sd.circle(center_position = point)
        X += 100
    Y += 100
    X = 600

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for o in range(100):
    point = sd.random_point()
    sd.circle(center_position = point)

sd.pause()