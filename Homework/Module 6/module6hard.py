from math import pi


class Figure:
    def __init__(self, color, sides_count=0, *sides, filled=bool):
        self.sides_count = sides_count
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *args):
        return all(isinstance(i, int) and i > 0 and len(args) == self.sides_count
                   for i in args)

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = [*args]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides) * self.sides_count


class Circle(Figure):
    def __init__(self, color, *sides, sides_count=1):
        self.sides_count = sides_count
        if len(sides) != 1:
            super().__init__(color, sides_count, 1)
        else:
            super().__init__(color, sides_count, *sides)
        self.__radius = sum(self.get_sides()) / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Cube(Figure):
    def __init__(self, color, *sides, sides_count=12):
        self.sides_count = sides_count
        if len(sides) != 1:
            super().__init__(color, sides_count, [1] * self.sides_count)
        else:
            super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())