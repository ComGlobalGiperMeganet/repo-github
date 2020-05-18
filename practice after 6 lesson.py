#----------------------------------------------------Задание 1----------------------------------------------------------
#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

class TrafficLight:
    __color = "red"

    def running(self):
        import time
        previous_color = ""
        while True:
            if self.__color == "red":
                print("\033[31m {}" .format(self.__color))
                time.sleep(7)
                self.__color = "yellow"
                previous_color = "red"
            elif self.__color == "yellow" and previous_color == "red":
                print("\033[33m {}" .format(self.__color))
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "yellow" and previous_color == "green":
                print("\033[33m {}" .format(self.__color))
                time.sleep(2)
                self.__color = "red"
            elif self.__color == "green":
                print("\033[32m {}" .format(self.__color))
                time.sleep(7)
                self.__color = "yellow"
                previous_color = "green"

a = TrafficLight()
a.running()

#----------------------------------------------------Задание 2----------------------------------------------------------
#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
#Например: 20м*5000м*25кг*5см = 12500 т
class Road:
    def __init__(self, length, width, weight=25, height=5):
        self._length = length
        self._width = width
        self._weight = weight
        self._height = height

    def calc_mass_asphalt(self):
        return f"При следующих параметрах:\nДлины полотна: {self._length}м.,\nШирины полотна: {self._width}м., \n" \
f"Массе 1 кв. м.: {self._weight}кг.\nВысоты: {self._height}\nМасса асфальта = "\
f"{self._length * self._width * self._weight * self._height/1000:.0f} т."

a = Road(5000, 20)
print(a.calc_mass_asphalt())

#----------------------------------------------------Задание 3----------------------------------------------------------
#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def full_name(self):
        return f"{self.name} {self.surname}"

    def salary_with_bonus(self):
        return f"Полная заработная плата (оклад + премия): {self._income['wage']+self._income['bonus']}"

a = Position("Иван","Иванов","главный ведущий старший прокрастинатор",100500,50000 )
print(a.full_name())
print(a.salary_with_bonus())
print(a.position)

#----------------------------------------------------Задание 4----------------------------------------------------------
#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.ride_speed = 0
        self.current_speed = 0

    def go(self, ride_speed):
        self.ride_speed = ride_speed
        try:
            if ride_speed <= self.max_speed and ride_speed > 0:
                import time
                start_speed = self.current_speed
                timer = 1
                if self.current_speed == 0:
                    print(f"автомобиль {self.name} трогается")
                    time.sleep(1.5)
                else:
                    print(f"автомобиль {self.name} начинает разгон с {self.current_speed} км/ч до {self.ride_speed} км/ч")
                    time.sleep(1.5)
                while start_speed < ride_speed:
                    start_speed += 1
                    print(f"текущая скорость: {start_speed} км/ч", end="")
                    time.sleep(timer)
                    print('\r', end="")
                    if timer > 0.1:
                        timer -= 0.1
                    elif timer > 0.05:
                        timer -= 0.01
                    else:
                        timer = 0.05
                print(f"разгон закончен, едем со скоростью: {int(ride_speed)} км/ч, максимально возможная скорость данного автомобился {int(self.max_speed)} км/ч")
                time.sleep(1.5)
                self.current_speed = self.ride_speed
            else:
                print("эта машина не способна ехать с такой скоростью")
        except TypeError:
            print("Вы ввели некорректное значение, введите целое положительное число")
    def show_speed(self):
        return self.current_speed

    def stop(self):
        import time
        print(f"{self.name} останавливается")
        time.sleep(1.5)
        self.ride_speed = 0

    def turn(self, direction):
        try:
            import time
            self.direction = direction
            turn_speed = 60
            acceleration_speed = 60
            timer = 0.5
            if direction.lower() in ["налево", "направо"]:
                if self.ride_speed > turn_speed and self.ride_speed > 0:
                    print(f"текущая скорость слишком высока для поворота,")
                    time.sleep(1.5)
                    print(f"сбрасываем скорость до {turn_speed}, поворачиваем {direction},")
                    time.sleep(1.5)
                    print(f"набираем снова скорость до {self.ride_speed}")
                    time.sleep(1.5)
                    while acceleration_speed < self.ride_speed:
                        acceleration_speed += 1
                        print(f"набираем скорость: {acceleration_speed}", end="")
                        time.sleep(timer)
                        print('\r', end="")
                        if timer > 0.1:
                            timer -= 0.05
                        elif timer > 0.05:
                            timer -= 0.01
                        else:
                            timer = 0.05
                    print(f"скорость набрана до {self.ride_speed}, продолжаем поездку")
                    time.sleep(1.5)
                elif self.ride_speed <= turn_speed and self.ride_speed > 0:
                    print(f"Поворачиваем {direction} и продолжаем поездку со скоростью {self.ride_speed}")
                    time.sleep(1.5)
                else:
                    print("для осуществления поворота автомобиль должен ехать, запустите его методом go")
                    time.sleep(1.5)
            else:
                print("укажите корректно направление поворота: направо, или налево")
        except TypeError:
            print("Введите направление поворота направо, или налево")


class TownCar(Car):
    def show_speed(self):
        speed_limit = 60
        if Car.show_speed(self) > speed_limit:
            print(f"Зафиксировано превышение скоростного режима на {int(self.current_speed) - int(speed_limit)}км/ч,\
 сбросьте скорость до разрешенных {speed_limit} км/ч")

class SportCar(Car):
    def show_speed(self):
        speed_limit = 100
        if Car.show_speed(self) < speed_limit and self.current_speed > 0:
            print(f"Моя бабуля ездит быстрее, всего {self.current_speed}км/ч")

class WorkCar(Car):
    def show_speed(self):
        speed_limit = 40
        if Car.show_speed(self) > speed_limit:
            print(f"Зафиксировано превышение скоростного режима на {int(self.current_speed) - int(speed_limit)}км/ч,\
 сбросьте скорость до разрешенных {speed_limit} км/ч")

class PoliceCar(Car):
    def flasher(self, status):
        import time
        self.status = bool(status)
        if status == True:
            counter = 0
            color = 0
            while counter < 10:
                if color == 0:
                    counter += 1
                    print("\033[31m {}".format(f"На автомобиле {self.name} работает мигалка"), end="")
                    time.sleep(0.5)
                    print('\r', end="")
                    color = 1
                else:
                    counter += 1
                    print("\033[34m {}".format(f"На автомобиле {self.name} работает мигалка"), end="")
                    time.sleep(0.5)
                    print('\r', end="")
                    color = 0
            print("\033[0m {}" .format(""))
        else:
            print("Мигалка выключена")
            time.sleep(0.5)

a = Car(250, "red", "unknow car", 0)
a.go(50)
a.turn("налево")
a.stop()
b = TownCar(150, "yellow", "skyline", 0)
b.go(100)
b.show_speed()
b.turn("направо")
b.stop
c = SportCar(350, "green", "350z", 0)
c.show_speed()
c.go(80)
c.show_speed()
d = PoliceCar(160, "blue", "Уаз", 1)
d.flasher(True)
d.flasher(0)

#----------------------------------------------------Задание 5----------------------------------------------------------
#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "запуск отрисовки"

class Pen(Stationery):
    def draw(self, text):
        self.text = text
        print("\033[34m {}".format(text+", написано ручкой"))

class Pencil(Stationery):
    def draw(self, text):
        self.text = text
        print("\033[2m\033[33m {}".format(text+", написано карандашом"))

class Handle(Stationery):
    def draw(self, text):
        self.text = text
        print("\033[1m\033[37m {}".format(text+", написано маркером"))

pen = Pen("Zebra")
pen.draw(pen.title)
pencil = Pencil("Кохинор")
pencil.draw(pencil.title)
marker = Handle("Перманентный маркер")
marker.draw(marker.title)
