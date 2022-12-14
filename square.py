class square():
    def __init__(self, width = '20',color = 'green'):
        print('Создаем квадрат: ')
        self._width = width
        self._color = color
        self._square = (int(width)) * (int(width))
    def __repr__(self):
        return ( str(self._width) + self._color + str(self._square))