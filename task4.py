# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_num = int(input('Введите число: '))
res = ''

while decimal_num > 0:
    res = str(decimal_num % 2) + res
    decimal_num = decimal_num // 2

print(res)
