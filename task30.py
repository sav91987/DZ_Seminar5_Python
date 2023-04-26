first_number = int(input('Введите первое число прогрессии: '))
step = int(input('Введите шаг прогрессии: '))
numbers = int(input('Введите число элементов прогрессии: '))

arith_progres = []
for i in range(numbers):
    arith_progres.append(first_number)
    first_number += step
print(arith_progres)
