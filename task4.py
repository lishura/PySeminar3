# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите десятичное число: '))
num_double = []
while num != 1:
    if num % 2 == 0:
        num_double.insert(0, 0)
    else:
        num_double.insert(0, 1)

    num = int(num/2)
num_double.insert(0, 1)
print(*num_double, sep='')
