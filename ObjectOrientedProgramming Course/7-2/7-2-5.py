class Summator:

    def __init__(self, base=1):
        self.base = base

    def total(self, n):
        return sum(i ** self.base for i in range(1, n + 1))


class SquareSummator(Summator):

    def __init__(self):
        super().__init__(2)


class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    pass