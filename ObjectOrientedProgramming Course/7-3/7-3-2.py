class LowerString(str):
    def __new__(cls, obj=None, **kwargs):
        if obj is None:
            obj = ''
        instance = super().__new__(cls, str(obj).lower(), **kwargs)
        return instance
