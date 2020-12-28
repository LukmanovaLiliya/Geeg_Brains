# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("file1.txt", "w", encoding = "UTF-8") as file1:
    while True:
        text = input("Введите текст: ")
        if text == "":
            break
        file1.write(f"{text}\n")

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file2.txt", "r", encoding = "UTF-8") as file2:
    count = [len(line.split()) for line in file2]
    print(f"В файле {len(count)} строк")
    print(f"Количество слов построчно: {count}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open("file3.txt", 'r', encoding = 'UTF-8') as file3:
    stuff = [line.split()[0] for line in file3 if int(line.split()[1]) < 20000]
    print(f"Сотрудники с окладом менее 20 тыс.: {stuff}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
my_dict = {
    "One" : "Один",
    "Two" : "Два",
    "Three" : "Три",
    "Four" : "Четыре"
}

new_file = []
with open("file4.txt", "r", encoding = "UTF-8") as file4:
    for i in file4:
        i = i.split(" ", 1)
        new_file.append(my_dict[i[0]] + " " + i[1])
    print(new_file)

with open("file4-2.txt", "w", encoding = "UTF-8") as file4_2:
    file4_2.writelines(new_file)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#
def my_sum():
    try:
        with open("file5.txt", "w", encoding="UTF-8") as file5:
            line = input("Введите цифры через пробел \n")
            file5.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print("Err!")

my_sum()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
with open("file6.txt", "r",  encoding = "UTF-8") as file6:
    lesson = file6.readlines()

def pars(str_lst):
    cnt = 0
    while cnt < len(str_lst):
        name = str_lst[cnt].split(':')[0]
        hr =  str_lst[cnt].split(':')[1]
        new_hr = str()
        for l in hr:
            try:
                l = int(l)
            except:
                if l != ' ':
                    new_hr = new_hr + ''
                else: new_hr = new_hr + ' '
            else:
                new_hr = (new_hr + str(l))
        new_hr = new_hr.split(' ')
        new_hr = [int(l) for l in new_hr if l != '']
        cnt += 1
        yield name, sum(new_hr)

my_dict = dict([l for l in pars(lesson)])
print(my_dict)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста
from json import dumps

results = [{}, {}]

try:
    with open("file7.txt", "r", encoding="utf-8") as file7:
        lines = file7.readlines()

    for line in lines:
        name, type_org, proceeds, cost = line.split()
        results[0][name] = int(proceeds) - int(cost)

    results[1]["averg"] = round(sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))

    with open("file7.json", "w", encoding="UTF-8") as filj7:
        filj7.write(dumps(results))
except IOError as e:
    print("Ошибка работы с файлом")
except ValueError:
    print("Err")
