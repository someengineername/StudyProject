class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}

    def base(self, name):
        return self.dic[name]

    def has_changed(self, name):
        return self.dic[name] != self.__dict__[name]

    def changed(self):
        return {k: self.dic[k] for k in self.fields if self.has_changed(k)}

    def save(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}
