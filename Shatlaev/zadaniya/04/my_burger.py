from typing import Any


class MyBurger:
    def __init__(self):
        self.ingridients = []
        self.receipt_1 = {'Бигмак': ['Булочка', 'Котлета', 'Огурчик', 'Помидорчик', 'Сыр', 'Майонез']}
        self.receipt_2 = {'Двойной чизбургер': ['Булочка', 'Котлета', 'Огурчик', 'Помидорчик', 'Сыр', 'Майонез', 'Котлета', 'Сыр']}
    def __add__(self, ingridient):
        print(f'А сейчас добавим {ingridient} в бургер')
        self.ingridients.append(ingridient)
        if ([self.ingridients] == list(self.receipt_1.values())):
            print(f'У вас получился {list(self.receipt_1.keys())[0]}')
            self.status = True
        elif ([self.ingridients] == list(self.receipt_2.values())):
            print(f'У вас получился {list(self.receipt_2.keys())[0]}')
            self.status = True
