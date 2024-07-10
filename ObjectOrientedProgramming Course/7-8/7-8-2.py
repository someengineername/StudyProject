class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:

    def __init__(self, input_list=None):

        if input_list is None:
            self.db = []
        else:
            self.db = [i for i in input_list]

    def add(self, item):
        self.db.append(item)

    def total(self):
        return sum([i.price for i in self.db])

    def remove(self, item):
        self.db = list(filter(lambda x: x.name != item, self.db))

    def __repr__(self):
        return '\n'.join([str(i) for i in self.db])
