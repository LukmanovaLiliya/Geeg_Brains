 # 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
# описанный метод.
#
from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(f"{TrafficLight.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
#
class Road:
    mass = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self):
        return f"{(self._length * self._width * self.mass * self.thickness)} т"

road = Road(20, 5000)

print(road.result())


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
        self._income["wage"] = income["wage"]
        self._income["bonus"] = income["bonus"]


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname} {self.position}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ps = Position("Петр", "Петров", "охранник", {"wage": 10000, "bonus": 500})
print(f"Сотрудник {ps.get_full_name()} зп составляет {ps.get_total_income()} в месяц")

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Автомобиль марки {self.name} {self.color} цвета поехал.\n"

    def stop(self):
        return f"Автомобиль марки {self.name} {self.color} цвета остановился.\n"

    def turn(self, direction):
        return f"Автомобиль марки {self.name} {self.color} цвета повернул {direction}.\n"

    def show_speed(self):
        return f"Автомобиль марки {self.name} {self.color} цвета движется со скоростью {self.speed}.\n"


class WorkCar(Car):
    def __init__(self, speed, color, name,):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return f"Автомобиль движется слишком быстро. Скорость составляет {self.speed}\n"
        else:
            return f"Автомобиль движется со скоростью {self.speed}\n"

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"Автомобиль движется слишком быстро. Скорость составляет {self.speed}\n"
        else:
            return f"Автомобиль движется со скоростью {self.speed}\n"


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar(65, "синего", "Reno Logan")
print(town.go(), town.show_speed(), town.turn("направо"), town.stop())

sport = SportCar(150, "черного", "BMW")
print(sport.go(), sport.show_speed(), sport.turn("налево"), sport.stop())

work = WorkCar(40, "серого", "Volga Siber")
print(work.go(), work.show_speed(), work.turn("налево"), work.stop())

police = PoliceCar(140, "бело-синего", "Toyota",  True)
print(police.go(), police.show_speed(), police.turn("направо"), police.stop())

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = "Stationery"

    def draw (self):
        return ("запуск отрисовки")

class Pen (Stationery):
    def draw (self):
        return ("Ручка")

class Pencil(Stationery):
    def draw(self):
        return ("Карандаш")

class Handle(Stationery):
    def draw(self):
        return ("Маркер")

Stationery = Stationery()
print(Stationery.draw())

Pen = Pen()
print(Pen.draw())

Pencil = Pencil()
print(Pencil.draw())

Handle = Handle()
print(Handle.draw())



