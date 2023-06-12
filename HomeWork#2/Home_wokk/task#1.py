#
# ✔ Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


# ВАЖНО
# Я писал решение довольно долго, и у меня слетала операционка, и все пропало, поэтому сдаю все с опозданием,
# полюс нужно успеть сделать следующе дз, задание с банком тоже слетело.
# К сожелению ч 3 дня не пушил в гит изменения, и очень этому расстроился, но это урок(теперь все храню в гит)

# В задание с банком я делал базу клиентов с хранением в sqlit3 и в, вложенных словарях
# (тут я дико запутался, поскольку мне нужно ыло взять данные из словаря обработать их и вернуть обратно в словарь).
# Поэтому я начал делать все через sqlit3, ну и все слетело, осталось только первоначальное решение


dict_ras = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}

num = 171  # число
step = 16  # степень


def dict123(arg):
    """ Функция поиска по словарю """
    if arg in dict_ras:
        return dict_ras.get(arg)


def convert(arg_num, arg_step):
    """ Функция более тривиальная она возвращает только цифры"""
    result = ''
    while arg_num > 0:
        result = str(arg_num % arg_step) + result
        arg_num = arg_num // arg_step
    return result


# Изначально сделал просто, но понял при расчете больших значений вывод не правильный
# и решил сделать буквы


# def convert_2(arg_num, result, converted_list=None):
#     while arg_num > 0:
#         list_on_num = dict123(result[0:2])
#         converted_list.append(list_on_num)
#         converted_list.reverse()
#     list_concatenation = ','.join(converted_list)
#     return f'{list_concatenation}'


def convert_3(arg):
    converted_list = []
    converted_list.append(arg)
    one_arg = converted_list[0:2]
    one_arg_2 = converted_list[2:]
    one_arg = dict123(str(one_arg))
    one_arg_2 = dict123(str(one_arg_2))
    list_concatenation = one_arg, one_arg_2
    print(list_concatenation)


# print(convert_2(num, step))
# print(convert(num, step))


pr = convert(num, step)

convert_3(str(pr))

if len(pr) >= 4:
    pass
    # convert_2(num, pr)
else:
    print(*pr)

#
# def convert_2(arg_num, arg_step, converted_list=[]):
#     """"Эта функция №2 которая возвращает более правильные ответы,
#     а именно буквы согласно правилами конвертирования они указаны в словаре"""
#     result = ''
#     while arg_num > 0:
#         result = str(arg_num % arg_step) + result
#         # в строку результат мы записываем все что не превышает двухзначный вывод(при вводе не больших значений)
#         if len(result) >= 2:
#             while len(result) == 2:
#                 # Проверяем если значение двухзначное
#                 list_on_num = dict123(result[0:2])
#                 converted_list.append(list_on_num)
#                 # проверяем две буквы по словарю если они есть, то записываем их в переменную
#                 converted_list.reverse()
#                 # разворачиваем список поскольку выше записываем в конец списка
#             list_concatenation = ','.join(converted_list)
#             return f'{list_concatenation}'
#     arg_num // arg_step
#     return result
#
#
# print(convert_2(num, step))

# if len(result) > 2:
#     list_concatenation = ','.join(converted_list)
#     print(list_concatenation)
# else:
#     print(result)

# Тут довольно долго мучался что бы сделать все по уму
