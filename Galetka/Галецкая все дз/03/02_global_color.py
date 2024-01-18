# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point1 = sd.get_point(100, 100)
point2 = sd.get_point(400, 100)
point3 = sd.get_point(100, 350)
point4 = sd.get_point(400, 350)
angle = 0
 
 
def triangle(point, angle_1, length, color):
    for angle in range(0, 360, 120):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v.draw(color=color)
        point = v.end_point
 
 
def square(point, angle_2, length, color):
    for angle in range(0, 360, 90):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v.draw(color=color)
        point = v.end_point
 
 
def pentagon(point, angle_3, length, color):
    for angle in range(0, 360, 72):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v.draw(color=color)
        point = v.end_point
 
 
def hexagon(point, angle_4, length, color):
    for angle in range(0, 360, 60):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v.draw(color=color)
        point = v.end_point
 
def figures_list():
    color = user_input()
    triangle(point=point1, angle_1=angle, length=100, color=color)
    square(point=point2, angle_2=angle, length=100, color=color)
    pentagon(point=point3, angle_3=angle, length=100, color=color)
    hexagon(point=point4, angle_4=angle, length=100, color=color)
 
 
colors = {
    '1': {'name': 'красный', 'color': sd.COLOR_RED},
    '2': {'name': 'оранжевый', 'color': sd.COLOR_ORANGE},
    '3': {'name': 'жёлтый', 'color': sd.COLOR_YELLOW},
    '4': {'name': 'зелёный', 'color': sd.COLOR_GREEN},
    '5': {'name': 'циан', 'color': sd.COLOR_CYAN},
    '6': {'name': 'голубой', 'color': sd.COLOR_BLUE},
    '7': {'name': 'фиолетовый', 'color': sd.COLOR_PURPLE}
}
 
 
def user_input():
    print('Возможные цвета:\n1 : красный \n2 : оранжевый \n3 : жёлтый \n4 : зелёный \n5 : '
          'циан \n6 : голубой \n7 : фиолетовый\n')
    while True:
        color = input('Введите желаемый цвет: ')
        if color in colors:
            color = colors['{}'.format(color)]
            return color
        else:
            print('Вы ввели некорректный номер:')
            continue
 
 
figures_list()

sd.pause()
