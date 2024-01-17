#файл 20 №1
"""
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month ==1 or month ==3 or month ==5 or month ==7 or month ==9 or month ==10 or month ==12:
    print('31 день')
elif month==2:
    print('28 дней')
elif month ==4 or month ==6 or month ==8 or month ==11:
    print('30 дней')
else:
    print('Номер месяца некорректен')"""



#файл 20 №2.1
"""
envelop_x, envelop_y = 10, 7
paper_x=int(input('Введите 1 сторону листа'))
paper_y=int(input('Введите 1 сторону листа'))
if paper_x<=envelop_x and  paper_y<=envelop_y:
    print('Да')
else:
    print('Нет')"""
#файл 20 №2.2
"""
hole_x = int(input('Введите длину прямоугольного отверстия'))
hole_y = int(input('Введите ширину прямоугольного отверстия'))
brick_x = int(input('Введите длину кирпича'))
brick_y = int(input('Введите ширину кирпича'))
brick_z = int(input('Введите высоту кирпича'))
if ((hole_x >= brick_x and hole_y >= brick_y) or (hole_x >= brick_y and hole_y >= brick_x) or
        (hole_x >= brick_x and hole_y >= brick_z) or (hole_x >= brick_z and hole_y >= brick_x) or
        (hole_x >= brick_y and hole_y >= brick_z) or (hole_x >= brick_z and hole_y >= brick_y)):
    print('да')
else: 
    print('Нет')"""
# файл 20 №3
"""
a=179
b=37
k=0
c=0
while a>0:
    k+=b
    if k>a:
        break
    c+=1
print(c)"""
#файл 20 №4
"""
educational_grant, expenses = 10000, 12000
n=9
k=expenses
c=expenses
while n!=0:
    k=k*1.03
    c+=k
    n-=1
print(c-100000)"""
""" файл 20 №5
goods = {
'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
item_of_goods = []
for product_name, product_code in goods.items():
    product_quantity = 0
    product_value = 0
    for position in store[product_code]:
        product_quantity+=position['quantity']
        product_value+=position['quantity']*position['price']
    print(product_name, '-', product_quantity, 'шт, стоимость', product_value, 'руб')
"""
#Файл 40 №1  ??
"""
room_1 = ["Яна", "Алёна", ]
room_2 = ["Иннокентий Петрович", ]
d=', '
s=', '
a=d.join(room_1)
b=s.join(room_2)
print("В комнате room_1 живут:", a)
print("В комнате room_2 живут:", b)"""
"""
spisok=[]
kolvo=int(input('Введите количество жителей'))
while kolvo>0:
    spisok.append(input('введите жителя'))
    kolvo-=1
d=', '
a=d.join(spisok)
print('На районе живут:', a)"""
#файл 40 №3
"""import my_burger
print('Cделай бургер')
ingrid=[my_burger.bulochka(), my_burger.kotleta(), my_burger.sir(), my_burger.sir()]
d=', '
a=d.join(ingrid)
print('Бургер состоит из:', a)"""
