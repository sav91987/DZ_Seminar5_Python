'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
'''


def get_pow(num_a, num_b):
    if abs(num_b) == 0:
        return 1
    elif abs(num_b) == 1:
        return num_a
    elif num_b<0:
        return 1 / (num_a * get_pow(num_a, abs(num_b) - 1))
    else:
        return num_a * get_pow(num_a, abs(num_b) - 1)
    
base = int(input('Введите основание: '))
degree = int(input('Введите степень: '))
    
print(f'Число {base} в степени {degree} равно: {get_pow(base, degree)}')