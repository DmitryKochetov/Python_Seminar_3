# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
fractional_list = []
result = 0

for i in list:
    if i != 0:
        fractional_list.append(round(i % 1, 5))

max_fract = fractional_list[0]
min_fract = fractional_list[0]

for i in fractional_list:
    if max_fract < i:
        max_fract = i
    if (min_fract > i and i > 0):
        min_fract = i

result = max_fract - min_fract
print(f'{fractional_list} => {result}')
