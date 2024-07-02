class DevelopmentTeam:

    def __init__(self):
        self.list_of_juniors = []
        self.list_of_seniors = []

    def add_junior(self, *args):
        self.list_of_juniors.extend(list(map(lambda x: (x, 'junior'), args)))

    def add_senior(self, *args):
        self.list_of_seniors.extend(list(map(lambda x: (x, 'senior'), args)))

    def __iter__(self):
        yield from self.list_of_juniors + self.list_of_seniors