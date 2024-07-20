import functools


def snake_case(attrs=False):
    def is_snake(input_string):

        from re import fullmatch

        if ' ' in input_string:
            return False

        match1 = fullmatch(r'[a-z0-9]+(?:_[a-z0-9]+)*', input_string)
        if match1:
            return True
        else:
            return False

    def to_snake(input_string):

        from re import split

        split1 = list(filter(lambda x: x != '', split(r'([A-Z][a-z]+)', input_string)))
        new_list = [data.lower() if number == 0 else str('_' + data.lower()) for number, data in enumerate(split1)]

        return ''.join(new_list)

    def wrapper(cls):

        if not attrs:

            list_to_work_with = [i for i in cls.__dict__ if
                                 not (len(i) > 4 and i.isascii() and i.startswith('__') and i.endswith(
                                     '__')) and callable(cls.__dict__[i])]

            for method_name in list_to_work_with:

                if not method_name.startswith('_'):

                    method_value = cls.__dict__[method_name]
                    if is_snake(method_name):
                        continue
                    else:
                        new_name = to_snake(method_name)

                    setattr(cls, new_name, method_value)
                    delattr(cls, method_name)
                else:
                    temp_name = method_name[1:]

                    method_value = cls.__dict__[method_name]

                    if not is_snake(temp_name):
                        new_name = to_snake(temp_name)
                        setattr(cls, str('_' + new_name), method_value)
                        delattr(cls, method_name)

        else:

            list_to_work_with = [i for i in cls.__dict__ if not (
                    len(i) > 4 and i.isascii() and i.startswith('__') and i.endswith('__')) and not callable(
                cls.__dict__[i])]
            for method_name in list_to_work_with:
                method_value = cls.__dict__[method_name]
                if is_snake(method_name):
                    continue
                else:
                    new_name = to_snake(method_name)

                setattr(cls, new_name, method_value)
                delattr(cls, method_name)

        return cls

    return wrapper
