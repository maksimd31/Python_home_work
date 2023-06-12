#
# ✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль
# fractions.


from fractions import Fraction

# Ввод дробей
fraction1 = input("Введите дроби: ")
# разбиваю на переменные.
per = list(fraction1)
fraction_one = per[0]
fraction_two = per[-1]


def convert_fraction_sum(fraction_one_arg, fraction_two_arg):
    """Посмотрел лекцию и переделал функцию, функция выполняет сложение дробей
    функция выполняет одну задачу, и как черный ящик возвращает результат"""
    sum_fraction = Fraction(fraction_one_arg) + Fraction(fraction_two_arg)
    return f'Сумма дробей: {sum_fraction}'


def convert_fraction_multiplication(fraction_one_arg, fraction_two_arg):
    """Посмотрел лекцию и переделал функцию, функция выполняет умножение дробей"""
    multiply_fraction = Fraction(fraction_one_arg) * Fraction(fraction_two_arg)
    return f'Произведение дробей: {multiply_fraction}'


# принты использовал вне функции
print(convert_fraction_sum(int(fraction_one), int(fraction_two)))
print(convert_fraction_multiplication(int(fraction_one), int(fraction_two)))
