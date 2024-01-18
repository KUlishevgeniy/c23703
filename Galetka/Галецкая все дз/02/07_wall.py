# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for row in rows:
    y1 += 50
    start_point = sd.get_point(0, y1)
    end_point = sd.get_point(600, y1)

    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_ORANGE, width=6)
    # Четная строка
    if row % 2 == 0:
        x_v_0 = 0
        x_v_1 = 0
        for row_v in range(7):
            start_point1 = sd.get_point(x_v_0, y_v_0)
            end_point1 = sd.get_point(x_v_1, y_v_1)
            sd.line(start_point=start_point1, end_point=end_point1, color=sd.COLOR_ORANGE, width=6)
            x_v_0 += width
            x_v_1 += width
    # Нечётная строка
    else:
        # Сдвиг
        x_v_0 = width / 2
        x_v_1 = width / 2
        for row_v in range(6):
            start_point1 = sd.get_point(x_v_0, y_v_0)
            end_point1 = sd.get_point(x_v_1, y_v_1)
            sd.line(start_point=start_point1, end_point=end_point1, color=sd.COLOR_ORANGE, width=6)
            x_v_0 += width
            x_v_1 += width

    # Закончили рисовать одну строку, увеличиваем координаты `y`
    y_v_0 += height
    y_v_1 += height

simple_draw.pause()
