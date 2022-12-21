# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
length = int(input('Введите длину списка: '))
my_list = []
for i in range(length):
    my_list.append(round(random.uniform(1, 10), 2))
new_list = [None]*length
for i in range(length):
    new_list[i] = round(my_list[i] % 1, 2)
    # new_list[i] = round(my_list[i]-int(my_list[i]),2)

max = new_list[0]
min = new_list[0]
for i in range(length):
    if new_list[i] > max:
        max = new_list[i]
    if new_list[i] < min:
        min = new_list[i]


print(my_list)

print(round(max-min, 2))
