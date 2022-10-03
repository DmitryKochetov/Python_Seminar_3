# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

fib_list = []


def nega_fib(n):
    if n == -1:
        return 1
    if n in [-2, -1]:
        return -1
    else:
        return nega_fib(n + 2) - nega_fib(n + 1)


def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for m in range(-8, 0):
    fib_list.append(nega_fib(m))

for i in range(8+1):
    fib_list.append(fib(i))

print(fib_list)
