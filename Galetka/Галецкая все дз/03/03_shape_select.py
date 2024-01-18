# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_figure(point, angle, length, incline):
    v2 = sd.get_vector(point, angle, length)
    cycles = round(360 / incline) - 1
    for _ in range(cycles):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angle += incline
    sd.line(start_point=point, end_point=v2.start_point, width=3)
 
 
def triangle(point, angle, length):
    incline = 120
    draw_figure(point, angle, length, incline)
 
 
def square(point, angle, length):
    incline = 90
    draw_figure(point, angle, length, incline)
 
 
def pentagon(point, angle, length):
    incline = 70
    draw_figure(point, angle, length, incline)
 
 
def hexagon(point, angle, length):
    incline = 60
    draw_figure(point, angle, length, incline)
 
 
def shape_parameters():
    triangle(point=sd.get_point(250, 250), angle=20, length=150)
    square(point=sd.get_point(250, 250), angle=20, length=150)
    pentagon(point=sd.get_point(250, 250), angle=20, length=100)
    hexagon(point=sd.get_point(250, 250), angle=20, length=100)
 
 
shape_list = {
    '1': 'figure_1',
    '2': 'figure_2',
    '3': 'figure_3',
    '4': 'figure_4',
}
 
 
def user_input():
    print('Возможные фигуры:\n1 : Треугольник \n2 : Квадрат \n3 : Пятиугольник \n4 : Шестиугольник')
    while True:
        user_shape = input('Введите желаемую фигуру: ')
        if user_shape in shape_list:
            shape = shape_list['{}'.format(user_shape)]
            return shape
        else:
            print('Вы ввели некорректный номер:')
            continue
 
 
shape_parameters()
sd.pause()


sd.pause()
