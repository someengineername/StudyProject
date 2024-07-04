class UpperPrintString(str):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __str__(self):
        return self.upper()
