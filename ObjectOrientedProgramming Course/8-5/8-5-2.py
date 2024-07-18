import functools

def add_attr_to_class(**attrs):
    def decorator(cls):

        for k, v in attrs.items():
            setattr(cls, k, v)

        return cls

    return decorator
