class NonKeyword:

    def __init__(self, attr):
        self._attr = attr

    def __set_name__(self, cls, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        import keyword

        if value in keyword.kwlist:
            raise ValueError('Некорректное значение')
        else:
            instance.__dict__[self._name] = value