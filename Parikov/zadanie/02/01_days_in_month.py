# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

monthes = {
    31: [1, 3, 5, 7, 8, 10, 12],
    30: [4, 6, 9, 11],
    28: [2]
}

for days, numbers in monthes.items():
    for j in numbers:
        if month == j:
            print(days, 'дней')
            break
