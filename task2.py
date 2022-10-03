# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_1 = [2, 3, 4, 5, 6, 7, 8, 2]
multiple_list = []
multiple_num = 1

for i in range(0, len(list_1)):
    if (i >= len(list_1)/2):
        break
   
    multiple_num = list_1[i] * list_1[len(list_1)-i-1]
    multiple_list.append(multiple_num)
   
print(f'{list_1} => {multiple_list};')

