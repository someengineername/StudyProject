import sys


class UpperPrint:

    def __enter__(self):
        self.original_stdout = sys.stdout.write
        sys.stdout.write = lambda x: self.original_stdout(x.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_stdout
