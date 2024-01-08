# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9

# TODO здесь ваш код

if paper_x <= envelop_x and paper_y <= envelop_y:
    print('ДА')
elif paper_x <= envelop_y and paper_y <= envelop_x:
    print('ДА')
else:
    print('НЕТ')

