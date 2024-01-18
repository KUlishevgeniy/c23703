user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if (month >= 1) and (month <= 12):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        print('31')
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        print('30')
    else:
        print('28')
else:
    print('Некорректный номер месяца')