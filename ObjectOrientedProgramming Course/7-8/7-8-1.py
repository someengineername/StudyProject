class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Circle:

    def __init__(self, radius, point):
        self.center = point
        self.radius = radius

    def __repr__(self):
        return f'({self.center.x}, {self.center.y}), r = {self.radius}'


point = Point(1, 1)
circle = Circle(5, point)

print(point)
print(circle)
