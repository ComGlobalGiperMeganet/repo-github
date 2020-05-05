#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [
            123,
            1.12,
            'abc',
            {'apple': 'яблоко', 'pear': 'груша', 'orange': 'апельсин'},
            (12, 24, 36, 48, 60),
            {1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd'},
            ['one', 'two', 'three', 'four', 'five'],
            True,
            False
            ]

count1 = 0
count2 = 0

for i in my_list:
    count1 += 1
    count2 = 0
    print(f"{count1}:", f"Значение: '{i}'",type(i))
    if type(i) == int or type(i) == float or type(i) == bool:
        continue
    for el in i:
        count2 += 1
        print(f" {count1}.{count2}:", f"Значение: '{el}'", type(el))

#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_from_user = []
some_text = "Введите желаемую длину создаваемого списка - целое число, не менее 2 и не более 20:"
count = 0
while count < 2 or count > 20:
    count = input(some_text)
    if count.isdigit():
        count = int(count)
    else:
        count = 0
    some_text = "Для продолжения введите целое положительое число, не менее 2 и не более 20:"

res = count
temp_var = 0
temp_ind = 0

elements_for_list = 0
list_from_user = []
while len(list_from_user) < res:
    elements_for_list = input(f"Введите любое количество элементов списка но не более {res:.0f} "
                                  "При вводе стоп слова - enough - создание списка завершится досрочно, "
                                  f"оставшееся количество элементов для ввода: {count:.0f}:")
    if elements_for_list == 'enough':
        break
    else:
        list_from_user.append(elements_for_list)
        count -= 1

print(f"Сформированный Вами исходный список данных: {list_from_user}")

for el in range(len(list_from_user)):
    if el%2 == 0:
        temp_var = list_from_user[el]
        temp_ind = el
    elif el%2 != 0:
        list_from_user[temp_ind] = list_from_user[el]
        list_from_user[el] = temp_var

print(f"Список после обмена соседними значениями: {list_from_user}")

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Через list:
month = int(input("Введите номер месяца:"))
while month <= 0 or month >12:
    month = int(input("Ошибка ввода, введите число от 1 до 12:"))

season_list = ['начало списка', 'зима', 'зима', 'весна', 'весна', 'весна',
               'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

months_list = ['начало списка', 'январь', 'февраль', 'март', 'апрель', 'май',
               'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

print(f"Введенный месяц - {months_list[month]} соответствует сезону: {season_list[month]}")


#Через dict:
month = int(input("Введите номер месяца:"))

dict_of_moths = {12: 'декабрь', 1: 'январь', 2: 'февраль',
                 3: 'март', 4: 'апрель', 5: 'май',
                 6: 'июнь', 7: 'июль', 8: 'август',
                 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь'}

season_dict = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
               6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}

while month <= 0 or month >12:
    month = int(input("Ошибка ввода, введите число от 1 до 12:"))

print(f"Вы ввели номер: {month} - {dict_of_moths.get(month)}, "
      f"сезон, к которому относится месяц - {season_dict.get(month)}")

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string_from_input = input("Введите строку для ее последующего разделения по словам:")
for ind, el in enumerate(string_from_input.split(" "), 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)


#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 1]
text1 = "Введите новый элемент списка в виде целого числа: "
user_input = ""
new_list = []
print(f"Первоначальный список: {my_list}")
while len(user_input) == 0:
    user_input = input(text1)
    if user_input == "stop":
        break
    elif True if user_input.isdigit() else (True if user_input[1:].isdigit() and user_input[0] == "-" else False):
        user_input = int(user_input)
        if user_input > max(my_list):
            my_list.insert(0, user_input)
            user_input = ""
            text1 = "Введите следующее число, либо остановите выполнение программы командой stop:"
            print(my_list)
            continue
        elif user_input < min(my_list):
            my_list.append(user_input)
            user_input = ""
            text1 = "Введите следующее число, либо остановите выполнение программы командой stop:"
            print(my_list)
            continue
        elif user_input in my_list:
            for ind, el in enumerate(my_list):
                if el == user_input:
                    new_list.append(ind)
                    my_list.insert(max(new_list) + 1, user_input)
                    user_input = ""
                    text1 = "Введите следующее число, либо остановите выполнение программы командой stop:"
                    print(my_list)
                    new_list = []
                    break
        else:
            for ind1, el1 in enumerate(my_list):
                if user_input < el1:
                    continue
                elif user_input > el1:
                    my_list.insert(ind1, user_input)
                    user_input = ""
                    text1 = "Введите следующее число, либо остановите выполнение программы командой stop:"
                    print(my_list)
                    break
    else:
        text1 = "Ошибка ввода, для продолжения введите целое число, либо завершите создание списка командой stop:"
        user_input = ""
print(f"Выполнение программы закончено, итоговый список: {my_list}")



#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

id_product = 1
list_db = []
product_info = {}

while True:
    product_info = {}
    text = "Введите тип товара:"
    user_input = input(text)
    if True if user_input.isdigit() else (True if user_input[1:].isdigit() and user_input[0] == "-" else False):
        text = "Ошибка ввода, повторите операцию"
        print(text)
        continue
    else:
        product_info['Тип товара'] = user_input
        while True:
            text = "Введите название товара:"
            user_input = input(text)
            if True if user_input.isdigit() else False:
                text = "Ошибка ввода, повторите операцию"
                print(text)
                continue
            else:
                product_info['Название'] = user_input
                while True:
                    text = "Введите цену товара:"
                    user_input = input(text)
                    if False if user_input.isdigit() else True:
                        text = "Ошибка ввода, повторите операцию"
                        print(text)
                        continue
                    else:
                        product_info['Цена'] = int(user_input)
                        while True:
                            text = "Введите количество товара:"
                            user_input = input(text)
                            if False if user_input.isdigit() else True:
                                text = "Ошибка ввода, повторите операцию"
                                print(text)
                                continue
                            else:
                                product_info['Количество товара'] = int(user_input)
                                while True:
                                    text = "Введите единицы хранения:"
                                    user_input = input(text)
                                    product_info['Единица хранения'] = user_input
                                    list_db.append((id_product, product_info))
                                    id_product += 1
                                    text = "Ввести следующий товар? да/нет"
                                    user_input = input(text)
                                    break
                            break
                    break
            break
    if user_input == 'да':
        continue
    else:
        break

analytics = {}
for e in list_db:
   for e1 in e:
       if type(e1) == dict:
           for e2 in e1.keys():
                analytics.setdefault(e2, [])

for e3 in list_db:
   for e4 in e3:
       if type(e4) == dict:
           for el in analytics.keys():
               analytics[el].append(e4[el])

for index, element in enumerate(analytics.items(), 1):
    print(index, element)