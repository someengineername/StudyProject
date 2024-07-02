class AttrDict:

    def __init__(self, input_dict=None):

        if input_dict is None:
            pass
        else:
            self.__dict__.update(input_dict)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __getattr__(self, item):
        return self.__dict__[item]

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __iter__(self):
        yield from self.__dict__

    def __setattr__(self, key, value):
        pass
