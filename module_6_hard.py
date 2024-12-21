class Figure:
    sides_count = 0
    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if type(side) != int and side <= 0:
                    return False
            return True

    def get_sides(self):
        return list(self.sides)

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.sides = new_sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, sides):
        super().__init__(__color, sides)
        self.set_sides(sides)
        self.sides = sides
        __radius = self.sides / 2 * 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, sides):
        super().__init__(__color, sides)
        self.set_sides(sides)
    def get_square(self):
        a, b, c = self.sides
        p = (a+b+c) / 2
        return (p*(p-a)*(p-b)*(p-c))**0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, sides):
        super().__init__(__color, sides)
        self.set_sides(*[sides] * self.sides_count)

    def get_volume(self):
        a = self.sides[0]
        return a ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())