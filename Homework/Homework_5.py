# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
#
from random import randint
my_list = [randint(3, 300) for i in range(30)]
for element in my_list:
    if element > 100:
        print(element, end=' ')
print()
print('Task_1')
#замени минусы на пробелы
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [randint(1,300) for i in range(30)]
my_results = []
for n in my_list:
        if n > 100:
            my_results.append(n)
print(my_results)
print('Task_2')
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [randint(3,300) for i in range(randint(1,30))]
if len(my_list)<2:
    my_list.append(0)
elif len(my_list)>=2:
    my_list.append(my_list[-1]+my_list[-2])
print(my_list)
print('Task_3')