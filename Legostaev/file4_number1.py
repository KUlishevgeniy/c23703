# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

from room_1 import folks
in1 = folks
from room_2 import folks
in2 = folks
print('в комнате room_1 живут:' + str(in1) + '\n'
      'в комнате room_2 живут:' + str(in2))
