class Reloopable:

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        temp1 = [i for i in self.file]
        return temp1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()