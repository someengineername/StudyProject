class TypeChecked:

    def __init__(self, *args):
        self.allowed_types = list(args)

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):

        if type(value) in self.allowed_types:
            instance.__dict__[self._name] = value
        else:
            raise TypeError('Некорректное значение')
