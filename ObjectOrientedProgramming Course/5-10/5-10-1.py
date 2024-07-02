class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self._color}')"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))