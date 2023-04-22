'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.'''


def get_sum(num_a, num_b):
    if num_a == 0:
        return num_b
    elif (num_a > 0 and num_b > 0) or (num_a > 0 and num_b < 0):
        return get_sum(num_a-1, num_b+1)
    elif (num_a < 0 and num_b < 0) or (num_a < 0 and num_b > 0):
        return get_sum(num_a+1, num_b-1)

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

print(f'Сумма чисел {first_num} и {second_num} равна {get_sum(first_num, second_num)}')