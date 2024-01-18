# -*- coding: utf-8 -*-
# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import district.central_street.house1 
import district.central_street.house2
import district.soviet_street.house1
import district.soviet_street.house2

villagers_room1 = [*district.central_street.house1.room1.folks,
             *district.central_street.house2.room1.folks,
             *district.soviet_street.house1.room1.folks,
             *district.soviet_street.house2.room1.folks
             ]
villagers_room2 = [*district.central_street.house1.room2.folks,
            *district.central_street.house2.room2.folks,
            *district.soviet_street.house1.room2.folks,
            *district.soviet_street.house2.room2.folks
            ]

print('В комнате room_1 живут:')
print(*villagers_room1, sep='\n')
print('\n')
print('В комнате room_2 живут:')
print(*villagers_room2, sep='\n')