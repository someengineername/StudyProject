import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self.__class__.__dict__['instances'].append(self)

    cls.__init__ = new_init

    return cls
