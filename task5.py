# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def negafib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negafib(n+2)-negafib(n+1)


num = int(input('Введите целое число: '))
result = []
for i in range(-num, 0):
    result.append(negafib(i))
for i in [0]:
    result.append(0)
for i in range(1, num+1):
    result.append(fib(i))

print(result)
