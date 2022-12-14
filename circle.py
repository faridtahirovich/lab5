from math import pi
class circle():
    def __init__(self, width = '20', radius = '18', color = 'red'):
        print('Создаем круг:')
        self._width = width
        self._radius = radius
        self._color = color
        self._square = pi * (int(radius)) * (int(radius))
    def __repr__(self):
        return (str(self._width) + str(self._radius) + str(self._color) + str(self._square))