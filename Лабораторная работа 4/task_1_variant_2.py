import math
from typing import Union
class Triangle:
    """Документация на базовый класс треугольника"""
    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param a: Длина стороны a
        :param b: Длина стороны b
        :param c: Длина стороны c
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Значение a должно быть типа int или float")
        if a <= 0:
            raise ValueError("Значение a должно быть больше 0")
        self.a = a
        if not isinstance(b, (int, float)):
            raise TypeError("Значение b должно быть типа int или float")
        if b <= 0:
            raise ValueError("Значение b должно быть больше 0")
        self.b = b
        if not isinstance(c, (int, float)):
            raise TypeError("Значение c должно быть типа int или float")
        if c <= 0:
            raise ValueError("Значение c должно быть больше 0")
        self.c = c

    def __str__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для чтения людьми

        :return: Строка для чтения людьми
        """
        return f"Треугольник со сторонами a = {self.a}, b = {self.b} и c = {self.c}"

    def __repr__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для машинно-ориентированного вывода

        :return: Строка для машинно-ориентированного вывода
        """
        return f"{self.__class__.__name__}(a={self.a}, b={self.b}, c={self.c})"

    def perimeter(self) -> Union[int, float]:
        """
        Функция, которая считает периметр треугольника.

        :return: Периметр треугольника
        """
        return self.a+self.b+self.c

    def area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь треугольника.

        :return: Площадь треугольника
        """
        p = self.perimeter()/2
        area = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return round(area, ndigits=2)

    def info(self) -> dict:
        """
        Функция возвращает обобщенную информацию об объекте (исходные данные, посчитанные периметр и площадь) в виде словаря с ключами "object", "perimeter" и "area"

        :return: Обобщенная информация об объекте в виде словаря

        Данный метод будет полностью унаследован дочерними классами, так как он универсальный
        """
        return {"object": str(self),
                "perimeter": self.perimeter(),
                "area": self.area()
                }

class Right_Triangle(Triangle):
    """Документация на дочерний класс прямоугольного треугольника"""
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прямоугольный треугольник"

        :param a: Длина катета a
        :param b: Длина катета b
        :param c: Параметр не требует заполнения (Длина гипотенузы c)
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Значение a должно быть типа int или float")
        if a <= 0:
            raise ValueError("Значение a должно быть больше 0")
        self.a = a
        if not isinstance(b, (int, float)):
            raise TypeError("Значение b должно быть типа int или float")
        if b <= 0:
            raise ValueError("Значение b должно быть больше 0")
        self.b = b

    def __str__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для чтения людьми

        :return: Строка для чтения людьми

        Метод перегружен, так как в данном классе для описания достаточно двух атрибутов
        """
        return f"Прямоугольный треугольник с катетами a = {self.a} и b = {self.b}"

    def __repr__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для машинно-ориентированного вывода

        :return: Строка для машинно-ориентированного вывода

        Метод перегружен, так как в данном классе для описания достаточно двух атрибутов
        """
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

    def perimeter(self) -> Union[int, float]:
        """
        Функция, которая считает периметр прямоугольного треугольника.

        :return: Периметр прямоугольного треугольника

        Выполнена перегрузка метода, так как для прямоугольного треугольника достаточно знать длины катетов, чтобы рассчитать длину гипотенузы
        """
        return self.a+self.b+math.sqrt(self.a**2+self.b**2)

    def area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь прямоугольного треугольника.

        :return: Площадь прямоугольного треугольника

        Выполнена перегрузка метода, так как для прямоугольного треугольника есть более простая формула для расчета плошади (половина произведения длин катетов)
        """
        area = self.a*self.b/2
        return round(area, ndigits=2)

class Regular_Triangle(Triangle):
    """Документация на дочерний класс равностороннего треугольника"""

    def __init__(self, a: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Равносторонний треугольник"

        :param a: Длина стороны a
        :param b: Параметр не требует заполнения, так как все стороны одинаковой длины
        :param c: Параметр не требует заполнения, так как все стороны одинаковой длины
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Значение a должно быть типа int или float")
        if a <= 0:
            raise ValueError("Значение a должно быть больше 0")
        self.a = a

    def __str__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для чтения людьми

        :return: Строка для чтения людьми

        Метод перегружен, так как в данном классе для описания достаточно одного атрибута
        """
        return f"Правильный треугольник со сторонами длиной a = {self.a}"

    def __repr__(self) -> str:
        """
        Функция, возвращающая строку, предназначенную для машинно-ориентированного вывода

        :return: Строка для машинно-ориентированного вывода

        Метод перегружен, так как в данном классе для описания достаточно одного атрибута
        """
        return f"{self.__class__.__name__}(a={self.a})"

    def perimeter(self) -> Union[int, float]:
        """
        Функция, которая считает периметр равностороннего треугольника.

        :return: Периметр равностороннего треугольника

        Выполнена перегрузка метода, так как равносторонний треугольник имеет стороны одинаковой длины
        """
        return 3*self.a

    def area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь равностороннего треугольника.

        :return: Площадь равностороннего треугольника

        Выполнена перегрузка метода, так как для равностороннего треугольника есть более простая формула для расчета плошади
        """
        area = math.sqrt(3)/4*self.a**2
        return round(area, ndigits=2)


if __name__ == "__main__":
    # Проверка работы классов
    triangle = Triangle(5, 10, 6)
    print(triangle)
    print(repr(triangle))
    print(triangle.perimeter())
    print(triangle.area())
    print(triangle.info())

    right_triangle = Right_Triangle(3, 4)
    print(right_triangle)
    print(repr(right_triangle))
    print(right_triangle.perimeter())
    print(right_triangle.area())
    print(right_triangle.info())

    regular_triangle = Regular_Triangle(6)
    print(regular_triangle)
    print(repr(regular_triangle))
    print(regular_triangle.perimeter())
    print(regular_triangle.area())
    print(regular_triangle.info())