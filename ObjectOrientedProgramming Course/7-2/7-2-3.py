class Triangle:

    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def perimeter(self):
        return sum(self.sides)


class EquilateralTriangle(Triangle):

    def __init__(self, side):
        self.sides = [side, side, side]
