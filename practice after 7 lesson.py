#-------------------------------------------------------Задание 1-------------------------------------------------------
#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_str = ""

    def __str__(self):
        for ind, el in enumerate(self.my_list):
            if ind > 0:
                self.my_str += "\n"
            for num in el:
                self.my_str += str(num)
                self.my_str += "   "
        return self.my_str + "\n"

    def __add__(self, other):
        my_str2 = ""
        el_max_len = 0
        for inner_list in self.my_list:
            if len(inner_list) > el_max_len:
                el_max_len = len(inner_list)
        for inner_list in other.my_list:
            if len(inner_list) > el_max_len:
                el_max_len = len(inner_list)
        for i, inner_list in enumerate(self.my_list):
            if len(inner_list) < el_max_len:
                for i2 in range(el_max_len - len(inner_list)):
                    self.my_list[i].append(0)
        for i, inner_list in enumerate(other.my_list):
            if len(inner_list) < el_max_len:
                for i2 in range(el_max_len - len(inner_list)):
                    other.my_list[i].append(0)

        if len(self.my_list) < max(len(self.my_list), len(other.my_list)):
            for i in range(max(len(self.my_list), len(other.my_list)) - len(self.my_list)):
                self.my_list.append([0 for i in range(el_max_len)])

        elif len(other.my_list) < max(len(self.my_list), len(other.my_list)):
            for i in range(max(len(self.my_list), len(other.my_list)) - len(other.my_list)):
                other.my_list.append([0 for i in range(el_max_len)])

        for ind1, el1 in enumerate(self.my_list):
            if ind1 > 0:
                my_str2 += "\n"
            for ind2, el2 in enumerate(el1):
                my_str2 += str(self.my_list[ind1][ind2] + other.my_list[ind1][ind2])
                my_str2 += "   "
        return my_str2 + "\n"


test_list1 = [[1,2,3],
              [4,6],
              [8,2,1]]

test_list2 = [[4,3,2],
              [1,-1,3,8]]

matrix1 = Matrix(test_list1)
matrix2 = Matrix(test_list2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)

#-------------------------------------------------------Задание 2-------------------------------------------------------
#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def total_tissue_consumption(self, param_1):
        pass

class Coat(Clothes):
    def total_tissue_consumption(self, size):
        self.v = size
        result = (self.v/6.5 + 0.5)
        return f"При размере {self.v}, общее количество необходимой ткани для пошива пальто: {result:.2f}"
    @property
    def size(self):
        return self.__v
    @size.setter
    def v(self, size):
        if size < 38:
            self.__v = 38
        elif size > 60:
            self.__v = 60
        else:
            self.__v = size

class Costume(Clothes):

    def total_tissue_consumption(self, height):
        self.h = height
        result = (2*self.h + 0.3)
        return f"При росте {self.h}, общее количество необходимой ткани для пошива костюма: {result:.2f}"
    @property
    def height(self):
        return self.__h
    @height.setter
    def h(self, height):
        if height < 140:
            self.__h = 140
        elif height > 210:
            self.__h = 210
        else:
            self.__h = height

my_costume = Costume()
my_coat = Coat()
print(my_costume.total_tissue_consumption(220))
print(my_costume.total_tissue_consumption(130))
print(my_costume.total_tissue_consumption(183))
print(my_coat.total_tissue_consumption(62))
print(my_coat.total_tissue_consumption(35))
print(my_coat.total_tissue_consumption(54))

#-------------------------------------------------------Задание 3-------------------------------------------------------
#Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
# до целого числа.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
#ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
class OrganicCell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __str__(self):
        return f"В структуре находится органических клеток: {self.num_of_cells:.0f}"

    def __add__(self, other):
        return f"После выполнения сложения в структуре находится органических клеток:\
{self.num_of_cells + other.num_of_cells:.0f}"

    def __sub__(self, other):
        return f"После выполнения вычитания в структуре находится органических клеток:\
{self.num_of_cells - other.num_of_cells:.0f}" if self.num_of_cells > other.num_of_cells else\
            f"Некорректные значения для выполнения операции"

    def __mul__(self, other):
        return f"После выполнения умножения в структуре находится органических клеток:\
{self.num_of_cells * other.num_of_cells:.0f}"

    def __truediv__(self, other):
        return f"После выполнения деления в структуре находится органических клеток:\
{self.num_of_cells / other.num_of_cells:.0f}" if self.num_of_cells > other.num_of_cells else \
            f"Некорректные значения для выполнения операции"

    def make_order(self, parts):
        cell = self.num_of_cells
        print()
        print("Делим ячейку на указанное количество частей:")
        for i in range((cell // parts + cell % parts)):
            if i > 0:
                cell -= parts
            if cell >= parts:
                print(parts * "*")
            elif cell > 0:
                print(cell * "*")

cell_1 = OrganicCell(24)
cell_2 = OrganicCell(18)
print(cell_1)
print(cell_2)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_2-cell_1)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_2/cell_1)
cell_1.make_order(5)
cell_2.make_order(6)
