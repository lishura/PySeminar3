# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
length = int(input('Введите длину списка: '))
my_list = []
for i in range(length):
    my_list.append(random.randint(-10, 10))
sum = 0
for i in range(length):
    if i % 2 == 1:
        sum += my_list[i]
print(my_list)
print('Сумма элементов на нечетных позициях равна ', sum)