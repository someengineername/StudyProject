from abc import ABC, abstractmethod


class Validator(ABC):
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

        if self.validate(value):
            instance.__dict__[self._name] = value

    @abstractmethod
    def validate(self, obj):
        pass


class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):

        if not (isinstance(obj, int) or isinstance(obj, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')

        if self.minvalue is not None and obj < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')

        if self.maxvalue and obj > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')

        return True


class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):

        if not isinstance(obj, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')

        if self.minsize and len(obj) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')

        if self.maxsize and len(obj) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')

        if self.predicate and not self.predicate(obj):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')

        return True
