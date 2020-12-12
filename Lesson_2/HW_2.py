# #Задание №1
res_list = ["example", 2.2, False]
for t in res_list:
    print(f"An element {t} has type {type(t)}")
#
#
# #Задание №2
t = input("Введите символы: ")
res_list = list(t)
k = len(res_list)

for i in range(0,k-1,2):
    t = res_list[i]
    res_list[i] = res_list[i+1]
    res_list[i+1] = t
print(res_list)


#Задание №3
# решение с dict
month = int(input("Введите номер месяца: "))
my_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
if month == 1 or month == 12 or month == 2:
    print(my_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(my_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(my_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(my_dict.get(4))
else:
    print("None")

# #решение с list
month = int(input("Введите номер месяца: "))
my_list = ['зима', 'весна', 'лето', 'осень']
if month in (12, 1, 2):
    print(my_list[0])
elif month in (3, 4, 5):
    print(my_list[1])
elif month in (6, 7, 8):
    print(my_list[2])
elif month in (9, 10, 11):
    print(my_list[3])
else:
    print("None")

#Задание 4

answer = input("Введите предложение: ")
words = (answer.split())
for p, t in enumerate(words, 1):
    print(p, t[0:10])

# Задание №5
# Возникли трудности с решением данной задачи. Не могу довести ее до ума.

rating = [7, 5, 5, 3, 2]
i = 0
print(rating)
answer = int(input("Введите число: "))
while i < len(rating):
    if 0 < rating[i] < answer:
        rating.insert(i, answer)
    break
    i = i + 1
else:
    rating.append(answer)
print(rating)