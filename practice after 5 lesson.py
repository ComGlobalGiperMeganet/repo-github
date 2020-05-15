#-------------------------------------------------Задание 1-------------------------------------------------------------
"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка."""

with open("homework5 task1.txt", "w", encoding="utf-8") as task1:
    x = input("введите данные для записи в файл:")
    while x != "":
        print(x, file=task1)
        x = input("введите следующую строку для записи, или завершите нажав ввод без ввода данных:")

#-------------------------------------------------Задание 2-------------------------------------------------------------
"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
Использую созданный в 1 задании файл"""

line_counter = 0
words_counter = 0
words_in_lines = {}
line_number = []
import re
with open("homework5 task1.txt", "r", encoding="utf-8") as task2:
    for line in task2:
        line_counter += 1
        words_counter = 0
        line_number.append(line_counter)
        for word in re.findall(r'\w+', line):
            words_counter += 1
            words_in_lines[line_counter] = words_counter
print(f"Всего строк: {len(line_number)}")
for el in line_number:
    print(f"В строке №{el} количество слов:{words_in_lines[el]}")

#-------------------------------------------------Задание 3-------------------------------------------------------------
"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
 (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

workers = []
salary = []
for_avg = []
with open("homework5 task3.txt", "r", encoding='cp1251') as task3:
    for line in task3:
        for el in line.split():
            if el.isalpha():
                workers.append(el)
            else:
                salary.append(float(el))

print("Следующие сотрудники имеют оклад менее 20 тыс.:")
for ind in range(len(workers)):
    if salary[ind] < 20000:
        for_avg.append(salary[ind])
        print(f"Фамилия: {workers[ind]}, оклад: {salary[ind]}")
print(f"средний доход этих сотрудников: {sum(for_avg)/len(for_avg):.2f}")
print(f"средний доход всех сотрудников: {sum(salary)/len(salary):.2f}")

#-------------------------------------------------Задание 4-------------------------------------------------------------
"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
#еобходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

my_dict = {"one": "один",
           "two": "два",
           "three": "три",
           "four": "четыре",
           "five": "пять",
           "six": "шесть",
           "seven": "семь",
           "eight": "восемь",
           "nine": "девять",
           "ten": "десять"
           }
numbers = []
words = []
translate_words = []
with open("homework5 task4.txt", "r", encoding='cp1251') as task4:
    for line in task4:
        for el in line.replace("–","").split():
            if el.isalpha():
                words.append(el)
            if el.isdigit():
                numbers.append(el)
with open("homework5 task4 - translate result.txt", "w", encoding="utf-8") as task4_2:
    for i in range(len(numbers)):
        translate_words.append(my_dict[words[i].lower()])
        print(f"{translate_words[i]} – {numbers[i]}", file=task4_2)


#-------------------------------------------------Задание 5-------------------------------------------------------------
"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open("homework5 task5.txt", "a", encoding="utf-8") as task5:
    try:
        x = input("Введите цифры через пробел:")
        while x != "q":
            nums_for_sum = []
            for nums in x.split():
                nums_for_sum.append(int(nums))
            print(f"сумма введенных значений: {sum(nums_for_sum)}, результат операции записан в файл")
            print(sum(nums_for_sum), file=task5)
            x = input("Введите следующие цифры:")
    except ValueError:
        print("Вы ввели некорректное значение, данная строка не попадет в итоговый результат")

sum_nums_in_file = []
with open("homework5 task5.txt", "r", encoding="utf-8") as task5:
    for el in task5:
        sum_nums_in_file.append(int(el))
print(f"Итоговая сумма всех введенных ранее значений: {sum(sum_nums_in_file)}")

#-------------------------------------------------Задание 6-------------------------------------------------------------
"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

subject = []
class_hours = {}
class_sum_hours = {}
temp_num_str = ""
line_counter = 0
with open("homework5 task6.txt", "r") as task6:
    for line in task6:
        line_counter += 1
        for ind, word in enumerate(line.split()):
            if ind == 0:
                subject.append(word.replace(":",""))
            elif ind > 0:
                for num in word:
                    if num.isdigit():
                        temp_num_str += num
            if temp_num_str != "":
                if subject[line_counter - 1] in class_hours.keys():
                    class_hours[subject[line_counter - 1]].append(int(temp_num_str))
                    temp_num_str = ""
                else:
                    class_hours[subject[line_counter - 1]] = [int(temp_num_str)]
                    temp_num_str = ""
for el in class_hours:
    class_sum_hours[el] = sum(class_hours[el])

print(class_sum_hours)


#-------------------------------------------------Задание 7-------------------------------------------------------------
"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
 содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""
firms = []
rev = []
costs = []
profit = []
counter = 0
sum_prof = 0
avg_profit = {}
firm_dict = {}
json_list = []
with open("homework5 task7.txt", "r") as task7:
    for line in task7:
        for ind, word in enumerate(line.split()):
            if ind == 0:
                firms.append(word)
            if ind == 2:
                rev.append(int(word))
            if ind == 3:
                costs.append(int(word))

for i, e in enumerate(firms):
    profit.append(rev[i] - costs[i])
    if profit[i] > 0:
        counter += 1
        sum_prof += profit[i]

avg_profit["average_profit"] = sum_prof / counter
for i in range(len(firms)):
    firm_dict[firms[i]] = profit[i]
json_list.append(firm_dict)
json_list.append(avg_profit)
print(json_list)

import json
with open("homework5 task7.json", "w") as task7_2:
    json.dump(json_list, task7_2)