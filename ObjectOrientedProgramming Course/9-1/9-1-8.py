import math


class Testpaper:

    def __init__(self, name, pass_scheme, pass_percentage):
        self.name = name
        self.pass_scheme = pass_scheme
        self.pass_percentage = int((pass_percentage)[:-1])


class Student:

    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test: Testpaper, answers: list):
        result_percentage = round((sum(list(map(lambda x: x[0] == x[1], zip(test.pass_scheme, answers)))) / len(
            test.pass_scheme)) * 100)

        if isinstance(self.tests_taken, str):
            if result_percentage >= test.pass_percentage:
                self.tests_taken = dict({test.name: str('Passed! ') + '(' + str(result_percentage) + '%)'})
            else:
                self.tests_taken = dict({test.name: str('Failed! ') + '(' + str(result_percentage) + '%)'})
        else:
            if result_percentage >= test.pass_percentage:
                self.tests_taken.update({test.name: str('Passed! ') + '(' + str(result_percentage) + '%)'})
            else:
                self.tests_taken.update({test.name: str('Failed! ') + '(' + str(result_percentage) + '%)'})