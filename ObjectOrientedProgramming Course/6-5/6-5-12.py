class TreeBuilder:

    def __init__(self):
        self.storage = dict()
        self.level = 0

    def __enter__(self):
        self.storage.setdefault(self.level, [])
        self.level += 1

    def add(self, item):
        self.storage.setdefault(self.level, []).append(item)

    def __exit__(self, exc_type, exc_val, exc_tb):
        temp = self.storage[self.level]
        self.storage[self.level] = []
        self.level -= 1

        if temp:
            self.storage[self.level].append(temp)

    def structure(self):
        if self.storage:
            return self.storage[0]
        else:
            return []
