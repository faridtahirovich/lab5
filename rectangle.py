class rectangle():
    def __init__(self, width = '20', height = '18', color = 'red'):
        print('Создаем прямоугольник: ')
        self._width = width
        self._height = height
        self._color = color
        self._square = int(width) * int(height)
    def __repr__(self):
        return (str(self._width) + str(self._height) + self._color + str(self._square))
        