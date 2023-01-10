# 1)У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

My_string = '0123456789'
result = []

for symbol_one in My_string:
    for symbol_two in My_string:
        result.append(int(symbol_one + symbol_two))

print(result)

# При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
# представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
# A
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *
n=int(input('Insert the height of figure A: '))
for h in range(n):
    for w in range(n*2-1):
        if w==n-h-1 or w==n-1+h or h==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
# B
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *

n=int(input('Insert the height of figure B: '))
for h in range(n):
    for w in range(h+1,n):
        print(' ', end=' ')
    for w in range(h):
        print('*', end=' ')
    for w in range(h+1):
        print('*',end=' ')
    print()
# C
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *                   *
#     *               *
#       *           *
#         *       *
#           *   *
#             *

n=int(input('Insert the height of figure C: '))
for h in range(n-1):
    for w in range(h+1,n):
        print(' ', end=' ')
    for w in range(h):
        print('*', end=' ')
    for w in range(h+1):
        print('*',end=' ')
    print()
for h in range(n-1,-1,-1) :
    for w in range(n*2-1):
        if w==n-h-1 or w==n-1+h or h==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
# D
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *         *         *
#     *       *       *
#       *     *     *
#         *   *   *
#           * * *
#             *
n=int(input('Insert the height of figure D: '))
for h in range(n-1):
    for w in range(h+1,n):
        print(' ', end=' ')
    for w in range(h):
        print('*', end=' ')
    for w in range(h+1):
        print('*',end=' ')
    print()
for h in range(n-1,-1,-1) :
    for w in range(n*2-1):
        if w==n-h-1 or w==n-1+h or h==n-1 or w==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()