# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
length = int(input('Введите длину списка: '))
my_list = []
for i in range(length):
    my_list.append(random.randint(-10, 10))

result = []
if length % 2 == 0:
    for i in range(int(length/2)):
        result.append(my_list[i]*my_list[-1-i])
else:
    for i in range(int(length/2)+1):
        result.append(my_list[i]*my_list[-1-i])
print(my_list)
print(result)
