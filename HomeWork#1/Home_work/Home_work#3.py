# ✔ Программа загадывает число от 0 до 1000.

# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#  from random import randint
#  num = randint(LOWER_LIMIT, UPPER_LIMIT)

import random

answer_input = random.randint(0, 1000)
print(answer_input)


def guess_the_number(answer, total=0):
    """Вариант №1 в функции"""
    while total < 10:
        gess = int(input('ваше предложение ?'))
        if gess == answer:
            print(f'Победа вы угадали число это было {answer}\nВы затратили {total} попыток')

        elif int(gess) > int(answer):
            print('Меньше')
            total += 1
            continue
        else:
            print('Больше')
            total += 1
            print(total)
            continue
        if total == 10:
            print(f'Вы проиграли вы истратили все {total} попытки ')
    print(f'Вы проиграли вы истратили все {total} попытки ')


guess_the_number(answer_input)

guesses_left_input = 10


def guess_the_number_2(guesses_left, answer):
    """Второй вариант, на убывание счетчика"""
    while guesses_left > 0:
        print(f'У вас осталось {guesses_left} попыток.')
        guess = int(input('Введите число: '))
        if guess == answer:
            print('Поздравляем, вы угадали число!')
            break
        elif guess < answer:
            print('Больше')
        else:
            print('Меньше')
        guesses_left -= 1

    if guesses_left == 0:
        print(f'К сожалению, вы не угадали число {answer}.')
