# 1. Написать калькулятор для простых операций(+,-,*,/,**),
# Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)
#

num1 = int(input('Please enter the first number: '))
action = input('Please enter choice:''+, -, *, /, ** : ')
num2 = int(input('Please enter the second number: '))
if action == '+':
    print(num1 + num2)
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    if num2 == 0:
        print('This is an invalid input ')
    else:
        print(int(num1 / num2))
elif action == '**':
    print(num1 ** num2)

# 2. По данному целому числу N распечатайте все квадраты натуральных чисел,
#  не превосходящие N, в порядке возрастания.
# Например:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 100     1 4 9 16 25 36 49 64 81 100

n = int(input('Введите значение, которое не должен привышать наибольший квадрат из диапазона: '))
for i in range(1,n):
    i = i**2
    if i >= n:
        break
    print(i, end=' ')

# # 3. Опреелить является ли введенное с клавиатуры число простым
# (делится без остатка только на себя и единицу)



num = int(input('Определить является ли введенное с число простым: '))
counter = 0
for i in range(2, (num // 2) + 1) :
    if num % i == 0 :
        counter += 1
if counter <= 0:
    print('Число простое.')
else:
    print('Число не простое')
