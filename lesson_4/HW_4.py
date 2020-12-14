
# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, a, b, c = argv

def pay_func(a, b, c):
    return (a * b) + c
print('%.2f'%(float(a) * float(b) + float(c)))


# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [l[i + 1] for i, k in enumerate(l) if len(l) > i + 1 and l[i] < l[i + 1]]

print(result)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([el for el in my_list if my_list.count(el) == 1])

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

def m_func(el1, el2):
    return el1*el2
my_list = [el for el in range(100, 1001, 2)]

print(reduce(m_func, my_list))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count
my_list = []
for i in count(3):
    if i > 10:
        break
    else:
        print(i)
        my_list.append(i)
print(my_list)

#  cycle
from itertools import cycle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in cycle(my_list):
    if count > 8:
        break
    print(i)
    count += 1
# #
#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def fact(n):
    c = 1
    for i in range(1, n+1):
        c = c * i
        yield c

try:
    n = int(input("Введите целое число: "))
except ValueError as err:
    print("Ошибка: ", err)
    exit()

f = 1

for el in fact(n):
    print(f'Факториал числа {f}! = {el}')
    f += 1

