# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6, 7, 8, 2]
multiple_list = []
multiple_num = 1

for i in range(0, len(list)):
    if (i >= len(list)/2):
        break
   
    multiple_num = list[i] * list[len(list)-i-1]
    multiple_list.append(multiple_num)
   
print(f'{list} => {multiple_list};')

