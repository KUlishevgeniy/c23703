# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as r_1
from room_2 import folks as r_2

print("В комнате room_1 живут:" + ','.join(r_1))
print("В комнате room_2 живут:" + ','.join(r_2))