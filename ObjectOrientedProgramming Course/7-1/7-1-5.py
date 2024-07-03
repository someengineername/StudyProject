class Validator:

    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):

    def is_valid(self):
        if isinstance(self.obj, int) or isinstance(self.obj, float):
            return True
        return False
