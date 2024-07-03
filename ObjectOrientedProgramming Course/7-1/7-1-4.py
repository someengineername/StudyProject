class User:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def skip_ads():
        return False


class PremiumUser(User):

    @staticmethod
    def skip_ads():
        return True
