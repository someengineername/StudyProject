class Suppress:

    def __init__(self, *args):
        self.exceptions_list = [i for i in args]
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions_list:
            self.exception = exc_val
            return True