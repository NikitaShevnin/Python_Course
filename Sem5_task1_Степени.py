# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a_base = int(input("Введите число: "))
b_exp = int(input("Введите его степень: "))

def exponentiation (a_base, b_exp):
    if (b_exp == 1):
        return (a_base)
    if (b_exp != 1):
        return (a_base * exponentiation (a_base, b_exp - 1))

print("Результат возведения в степень равен:", exponentiation (a_base, b_exp))
