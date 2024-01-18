# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10 no
# brick_x, brick_y, brick_z = 10, 11, 2 no
# brick_x, brick_y, brick_z = 10, 2, 11 no
# brick_x, brick_y, brick_z = 2, 10, 11 no
# brick_x, brick_y, brick_z = 2, 11, 10 no
# brick_x, brick_y, brick_z = 3, 5, 6 yes
# brick_x, brick_y, brick_z = 3, 6, 5 yes
# brick_x, brick_y, brick_z = 6, 3, 5 yes
# brick_x, brick_y, brick_z = 6, 5, 3 yes
# brick_x, brick_y, brick_z = 5, 6, 3 yes
# brick_x, brick_y, brick_z = 5, 3, 6 yes
# brick_x, brick_y, brick_z = 11, 3, 6 yes
# brick_x, brick_y, brick_z = 11, 6, 3 yes
# brick_x, brick_y, brick_z = 6, 11, 3 yes
# brick_x, brick_y, brick_z = 6, 3, 11 yes
# brick_x, brick_y, brick_z = 3, 6, 11 yes
# brick_x, brick_y, brick_z = 3, 11, 6 yes
# (просто раскоментировать нужную строку и проверить свой код)

if ((brick_x < hole_x and brick_y < hole_y) or (brick_x < hole_y and brick_y < hole_x) or (brick_x < hole_x and brick_z < hole_y) or (brick_x < hole_y and brick_z < hole_x) or (brick_z < hole_x and brick_y < hole_y) or (brick_y < hole_x and brick_z < hole_y)):
    print("YES")
else:
    print("NO")
