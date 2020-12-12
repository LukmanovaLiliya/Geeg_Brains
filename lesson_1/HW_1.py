
print("Задание №1")
a = 7
b = 2.3
t = False

result = a, b, t
print(result)

fv_num = input("Ваше любимое число: ")
bd = input("Когда вы родились? ")
city = input("В каком городе вы живете? ")

print("Задание №2")
time = int(input("Введите время в секундах: "))
ss = (time % 60)
mm = (time//60) % 60
hh = (time//3600)
print("Время в секундах составит: %02d: %02d: %02d" % (hh, mm, ss))

print("Задание №3")
any_number = int(input("Введите любое число: "))
num = str(any_number)
l1 = num + num
l2 = num + num + num
result = any_number + int(l1) + int(l2)
print(f"Сумма чисел: {any_number} + {l1} + {l2}=", result)

print("Задание №4")
any_number = int(input("Введите любое положительное число: "))
m = any_number % 10
any_number = any_number//10
while any_number > 0:
    if any_number % 10 > m:
        m = any_number % 10
        any_number = any_number//10
print("Самая большая цифра в числе: %d " % (m))

print("Задание №5")

receipts = float(input("Введите сумму выручки компании: "))
cost = float(input("Введите сумму издержек компани: "))
dif = receipts - cost
if dif > 0:
    print("Ваша компания приносит прибыль")
    prf = dif/receipts*100
    per = "%"
    print("Рентабельность составляет: %d %s" % (prf, per))
    staff = float(input("Сколько человек работает в компании? "))
    result = dif/staff
    print("Прибыль фирмы в расчете на 1 сотрудника %d :" % (result))
if dif < 0:
    print("Ваша компания терпит убытки")
if dif == 0:
    print("Компания на 0")

print("Задание №6")
a = int(input("Результат 1-го дня: "))
b = int(input("Лучший результат: "))
day = 1
while a < b:
    a = a + (a * 0.1)
    day += 1
print("Лучший результат будет достигнут на %d день" % (day))

