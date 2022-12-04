# Задание №1. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = input("Введите последовательность чисел через запятую : ").split(',')
for i in range( len(arr) ):
    arr[i]=int(arr[i])

p = len(arr)//2 + len(arr)%2

res = []
for i in range(p):
    res.append( arr[i] * arr[ len(arr)-i-1 ] )
print(res)
















# lst_in = [int(i) for i in lst]
# lst_1 = []

# len_count = len(lst_in)
# len_count = int(len_count/2) + len_count%2

# for i in range(len_count): 
#     lst_1.append(lst_in[i]*lst_in[i*-1-1])
# print (lst_1)