class HtmlTag:
    indentor = -1

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        self.__class__.indentor += 1
        print(self.__class__.indentor * '  ' + f'<{self.tag}>', end='' if self.inline else '\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.inline:
            print(f'</{self.tag}>')
        else:

            print(self.__class__.indentor * '  ' + f'</{self.tag}>')
        self.__class__.indentor -= 1

    def print(self, text):
        if self.inline:
            print(text, end='')
        else:
            print('  ' + self.__class__.indentor * '  ' + text)
