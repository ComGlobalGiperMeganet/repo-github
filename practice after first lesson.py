#1 Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input("Представьтесь, пожалуйста: ")
count = 0
i = 4
org_password = input(f"Придумайте пароль:")

while count < 3:
    count += 1
    if org_password == "0" or org_password == "qwerty" or org_password == "12345":
        if i - count == 3:
            x = "попытки"
        elif i - count == 2:
            x = "попытки"
        elif i - count == 1:
            x = "попытка"
        org_password = input(f"Слишком простой пароль, придумайте сложнее, у вас есть {i - temp1} {x}:")
    else:
        break
if org_password == "0" or org_password == "qwerty" or org_password == "12345":
    print(f"{name}, Ваш пароль не соответствует заявленным требованиям, в доступе отказано.")
else:
    password = input("Ведите пароль для входа:")
    if password != org_password:
        print("Некорректный пароль - в доступе отказано")
    else:
        print(f"Добрый день {name}! пароль верный - добро пожаловать!")

#2 Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах:"))
h = time / 60 // 60
m = time / 60 % 60
s = time / 60 % 60 * 60 % 60
if h < 10:
    a1 = 0
else:
    a1 = ""
if m < 10:
    a2 = 0
else:
    a2 = ""
if s < 10:
    a3 = 0
else:
    a3 = ""

print(f"{a1}" + f"{h:.0f}:"+ f"{a2}" + f"{m:.0f}:"+ f"{a3}" + f"{s:.0f}")


#3  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите целое число:")
print(int(n) + int(str(n)*2) + int(str(n)*3))


#4 Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

max_num = 0
x = int(input("Введите целое положительное число:"))
while x != 0:
    if max_num == 9:
        break
    elif max_num < x%10:
        max_num = x%10
        x //= 10
    else:
        x //= 10

print(max_num)


#5 Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите выручку:"))
cost = int(input("Введите издержки:"))
if revenue > cost:
    print("Компания получает прибыль, так как выручка превышает расходы.")
    print(f"Рентабельность составляет {(revenue - cost)/revenue*100:.1f}%")
    prof_per_empl = (revenue - cost) / int(input("Введите числинность сотрудников компании:"))
    print(f"Прибыль в расчете на одного сотрудника составляет: {prof_per_empl:.0f}")
elif revenue < cost:
    print("Компания терпит убытки, так как издержки превышают выручку.")


#6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input("Введите расстояние пробежки в 1 день в км:"))
b = int(input("Введите желаемый результат км:"))
result = 1.1
days = 1

while a < b:
    days += 1
    a *= result

print(f"на {days:.0f}-й день спортсмен достиг результата - не мнее {b:.0f} км.")