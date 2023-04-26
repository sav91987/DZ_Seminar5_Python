import random
num_n = int(input('Введите число элементов: '))
min_num = int(input('Введите нижнюю границу проверяемого диапазона: '))
max_num = int(input('Введите верхнюю границу проверяемого диапазона: '))


print(my_list := [random.randint(-5, 10) for i in range(num_n)])
print(index_list := [i for i in range(num_n) if min_num < my_list[i] < max_num])