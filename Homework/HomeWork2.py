# 1. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
#  Сколько яблок останется в корзинке?
#  Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа)


Students = int(input('Student_in_school: '))

Apples = int(input('Apples_in_Basket: '))

Amount_of_apples = (Apples // Students)

print(f'Each students will receive', Amount_of_apples, 'apple')

Keep_in_basket = (Apples % Students)
print(f'number of apples will be left in a basket', Keep_in_basket)



# 2. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят
# в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

Math_ClassRoom_1 = int(input('How many students in 1 class:'))

Math_ClassRoom_2 = int(input('How many students in 2 class:'))

Math_ClassRoom_3= int(input('How many students in 3 class:'))

head_count_students = int(Math_ClassRoom_1+Math_ClassRoom_2+Math_ClassRoom_3)
print(f'We have', head_count_students,'students')

Table = round(head_count_students /2 )
print(f'We need', Table, 'desks')


# 3. Дано целое, положительное, трёхзначное число. Например: 123, 867, 374.
# Необходимо его перевернуть. Например, если ввели число 123,
#  то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. Строки использовать НЕЛЬЗЯ!
#

number_1 = int(input('Value for 3 digit number:'))
number_2 = number_1 % 10 * 100
number_3 = number_1 // 10
number_3 = number_3 % 10 * 10
number_4 = number_1 // 10 // 10
print(number_2+number_3+number_4)