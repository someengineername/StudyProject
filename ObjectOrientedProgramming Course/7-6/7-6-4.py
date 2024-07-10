class Meta:

    def __init__(self, mood='neutral'):
        self.mood = mood


class Father(Meta):

    @staticmethod
    def greet():
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Meta):

    @staticmethod
    def greet():
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass