ingredients = {
    'bun': False,
    'cutlet': False,
    'cucumber': False,
    'tomato': False,
    'mayonnaise': False,
    'cheese': False,
    'sauce': False
}


def add_bun(current_ingredients):
    current_ingredients['bun'] = True
    print('Положим булочку')
    return True


def add_cutlet(current_ingredients):
    if current_ingredients['bun']:
        current_ingredients['cutlet'] = True
        print('А теперь положим котлету')
        return True
    else:
        print('Неверный порядок')
        return False


def add_cucumber(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['cucumber'] = True
        print('Затем добавим огурчик')
        return True
    else:
        print('Неверный порядок')
        return False


def add_tomato(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['tomato'] = True
        print('Теперь добавляем помидорчик')
        return True
    else:
        print('Неверный порядок')
        return False


def add_cheese(current_ingredients):
    if current_ingredients['bun']:
        current_ingredients['cheese'] = True
        print('Добавляем сыр')
        return True
    else:
        print('Неверный порядок')
        return False


def add_mayonnaise(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['mayonnaise'] = True
        print('После добавим майонез')
        return True
    else:
        print('Неверный порядок')
        return False


def add_sauce(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['sauce'] = True
        print('Соус')
        return True
    else:
        print('Неверный порядок')
        return False