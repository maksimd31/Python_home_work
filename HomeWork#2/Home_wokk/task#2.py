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
fraction1 = input("Введите первую дробь: ")
fraction2 = input("Введите вторую дробь: ")

a, b = map(int, input('Введите дроби через пробел').split())


def convert_fraction(fraction_one, fraction_two):
    one = Fraction(fraction_one)
    tow = Fraction(fraction_two)
    sum_fraction = one + tow
    multiply_fraction = one * tow
    return f'Сумма дробей: {sum_fraction}\n Произведение дробей: {multiply_fraction}'


convert_fraction(a, b)
