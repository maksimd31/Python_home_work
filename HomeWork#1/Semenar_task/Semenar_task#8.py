# Задание No8
# 📌 Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# 📌 Пример результата:
# Сколько рядов у ёлки? 5
# *
# ***
# *****
# *******
# *********

print('''
    *
   ***
  *****
 *******
*********
''')

el = input('сколько рядов у елки?')

print('Молодец!\nУмеешь считать!' if el == 5 else 'Увы это не правильный ответ!')