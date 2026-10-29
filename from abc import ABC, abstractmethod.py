from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """площадь"""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


def pritn_area(shapes):
    for index, shape in enumerate(shapes, start=1):
        class_name = shape.__class__.__name__
        print("Фигура : ", index, class_name,"площадь : ", shape.area())

if __name__ == "__main__":
    shapes_list = [
        Rectangle(5, 4),
        Circle(4),
        Triangle(2, 3, 4)
    ]
    pritn_area(shapes_list)


# ===============================================

def send_not(sender, message):
    try:
        sender.send(message)
    except AttributeError:
        class_name = sender.__class__.__name__
        print("проверьте объект , он должен иметь метод send")


class EmailSender:
    def send(self, message):
        print("Email, сообщение : ", message)

class SmsSender:
    def send(self, message):
        print("Sms, сообщение : ", message)

class Classs:
    pass

if __name__ == "__main__":
    email = EmailSender()
    sms = SmsSender()
    error_object = Classs()
    text = "это сообщение"

    send_not(email, text)
    send_not(sms, text)
    send_not(error_object, text)


# ======================================================

class OS:
    def __init__(self, req_memory):
        self.req_memory = req_memory

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self, os_obj, ram_obj):
        self.os = os_obj
        self.ram = ram_obj

    def start(self):
        if self.os is None:
            print("ошибка запуска: OS отсутствует")
            return
        
        if self.ram is None:
            print("ошибка запуска : оперативная память (RAM) не установлена")
            return

        if self.ram.size < self.os.req_memory:
            print(f"ошибка запуска : недостаточно памяти. Требуется : {self.os.req_memory} ГБ, а установлено всего : {self.ram.size} ГБ")
            return
        print("компьютер успешно запущен, система готова к работе")


if __name__ == "__main__":
    print("--- Тест 1 ---")
    my_os = OS(5)
    my_ram = RAM(32)
    my_computer = Computer(my_os, my_ram)
    my_computer.start()

    weak_ram = RAM(2)
    broken_computer = Computer(my_os, weak_ram)
    broken_computer.start()

    no_ram_computer = Computer(my_os, None)
    no_ram_computer.start()

# ===========================================

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, number):
        return Vector2(self.x * number, self.y * number)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

if __name__ == "__main__":
    v1 = Vector2(2, 3)
    v2 = Vector2(4, 5)

    print("v1 =", v1)
    print("v2 =", repr(v2))

    print("v1 + v2 =", v1 + v2)
    print("v1 - v2 =", v1 - v2)
    print("v1 * 5 =", v1 * 5)

    v3 = Vector2(2, 3)
    print("v1 == v2 :", v1 == v2)
    print("v1 == v3 :", v1 == v3)
