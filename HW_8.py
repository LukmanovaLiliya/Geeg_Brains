# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return "Неккоректно введены данные"

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date = (int(year), int(month), int(day))
            return "Данные верны"
        except ValueError:
            return "Неккоректно введены данные"

print(Data.type("26-13"))
print(Data.valid("26-12-2020"))

# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class My_Error(Exception):
    def __init__(self, number):
        self.number = number


def div():
    try:
        num_1 = int(input("Введите делимое: "))
        num_2 = int(input("Введите делитель: "))
        if num_2 == 0:
            raise My_Error("Делить на ноль нельзя!")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Введите корректное число"
    except My_Error as err:
        return err


print(div())

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
# только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя
# данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
# вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна
# завершаться.
class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        while True:
            try:
                try:
                    user_val = int(input("Введите число: "))
                    ex = input(f"Число {user_val} добавлено в список. Введите еще число или отправьте слово 'stop': ").lower()
                    self.my_list.append(user_val)
                    if ex == "stop":
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Не корректно введены данные! Введите еще число или отправьте слово 'stop' : ").lower()
                if ex == "stop":
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные
# для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Ware_House:
    def __init__(self, name):
        self.name = name
        pass

class Office_Equipment:

    def __init__(self, name, model, price: float, quantity: int):
        self.name = name
        self.price = price
        self.model = model
        self.quantity = quantity

    def ship(self):
        try:
            name = input(f"Введите наименование: ")
            price = int(input(f"Введите цену за ед: "))
            quantity = int(input(f"Введите количество: "))
            self.items = {"Наименование устройства": self.name, "Модель устройства": self.model, "Цена": self.price,
                          "Количество":  self.quantity}
                item = {"Наименование устройства": name, "Цена за ед": price, "Количество": quantity}
            #  self.items.update(item)
            print(self.items)
        except ValueError:
            print("Недопустимое значение!")


class Printer(Office_Equipment):
    def __init__(self, name, model, price, quantity, serial_number):
        super().__init__(name, model, price, quantity)
        self.serial_number = serial_number


class Scanner(Office_Equipment):
    def __init__(self, name, model, price, quantity, serial_number, speed):
        super().__init__(name, model, price, quantity)
        self.serial_number = serial_number
        self.speed = speed


class Copy_Machine(Office_Equipment):
    def __init__(self, name, model, price, quantity, serial_number, speed):
        super().__init__(name, model, price, quantity)
        self.serial_number = serial_number
        self.speed = speed


printer = Printer("Samsung", 2TW, 3000, 5, 265)
scanner = Scanner("XP", 5400-0, 4500, 1, 102, 458)
copy_machine = Copy_Machine("Xerox", 400, 4892, 3, 5122, 45)
Printer.ship()
scanner.ship()
copy_machine.ship()

# что-то сложная задача для меня...не до конца разобралась с ней....ох, уж этот Питон, кусается пока!
#
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма равна: {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"


c_1 = Complex_Number(2, 8)
c_2 = Complex_Number(5, 10)
print(c_1 + c_2)
print(c_1 * c_2)