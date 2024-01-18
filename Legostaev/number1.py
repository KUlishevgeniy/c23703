# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
# TODO здесь ваш код
if 1 <= month < 8:
    if month % 2 == 1:
        print(31)
    elif month % 2 == 0 and month != 2:
        print(30)
    else:
        print(28)
elif 8 <= month <= 12:
    if month % 2 == 1:
        print(30)
    elif month % 2 == 0:
        print(31)
else: print('error')
