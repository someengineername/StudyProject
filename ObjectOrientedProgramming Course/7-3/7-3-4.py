class TitledText(str):

    def __new__(cls, str, title):
        instance = super().__new__(cls, str)
        instance.text_title = title
        return instance

    def title(self):
        return self.text_title
