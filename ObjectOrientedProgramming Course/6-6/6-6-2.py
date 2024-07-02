from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    reserved_output = sys.stdout.write
    sys.stdout.write = lambda x: reserved_output(x[::-1])
    yield
    sys.stdout.write = reserved_output
