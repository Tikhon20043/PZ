#Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
#класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
#переопределите методы, связанные с вычислением площади и периметра.

class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Figure):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return 4 * self.width


# Создаем объекты
rect = Rectangle(5, 3)
square = Square(4)

# Вычисляем площади и периметры
print(f"Площадь прямоугольника: {rect.area()}")
print(f"Периметр прямоугольника: {rect.perimeter()}")
print(f"Площадь квадрата: {square.area()}")
print(f"Периметр квадрата: {square.perimeter()}")