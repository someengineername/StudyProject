class LoopTracker:

    def __init__(self, itarable):
        self.iterable = iter(itarable)
        self.list_of_iterable = list(self.iterable)
        self.counter = -1
        self._accesses = 0
        self._empty_accesses = 0
        self._last_memory = None

    def __iter__(self):
        return self

    def __next__(self):

        self.counter += 1

        try:
            self._accesses += 1
            self._last_memory = self.list_of_iterable[self.counter]
            return self.list_of_iterable[self.counter]
        except:
            self._empty_accesses += 1
            self._accesses -= 1
            raise StopIteration

    @property
    def accesses(self):
        return self._accesses

    @property
    def first(self):
        try:
            return self.list_of_iterable[0]
        except:
            self._empty_accesses += 1
            raise AttributeError("Исходный итерируемый объект пуст")

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def last(self):

        if self._last_memory is None:
            raise AttributeError('Последнего элемента нет')
        else:
            return self._last_memory

    def is_empty(self):
        if self.counter == len(self.list_of_iterable) - 1:
            return True
        return False
