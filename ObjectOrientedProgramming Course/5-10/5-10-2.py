class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __hash__(self):
        sum_hash_keys = sum([hash(i) for i in self.__dict__.keys()])
        sum_hash_values = sum([hash(i) for i in self.__dict__.values()])
        sum_hash_pos = hash(''.join([str(i) for i in self.__dict__.keys()]))

        return sum_hash_keys + sum_hash_values + sum_hash_pos

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__ and list(self.__dict__) == list(other.__dict__)
        return NotImplemented

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        temp_row = 'Row(' + ', '.join(
            [str(str(k) + '=' + str("'" + str(v) + "'") if isinstance(v, str) else
                 str(k) + '=' + str(v)) for k, v in
             self.__dict__.items()]) + ')'
        return temp_row

    def __setattr__(self, key, value):

        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            raise AttributeError('Установка нового атрибута невозможна')

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return object.__getattribute__(self, item)