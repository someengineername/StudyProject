from abc import ABC, abstractmethod


class AbstractStat(ABC):

    def __init__(self, iterable=None):
        if iterable is None:
            self.itt = []
        else:
            self.itt = iterable

    def add(self, n):
        self.itt.append(n)

    def clear(self):
        self.itt = []

    @abstractmethod
    def result(self):
        pass


class MinStat(AbstractStat):

    def result(self):
        if self.itt:
            return min(self.itt)
        else:
            return None


class MaxStat(AbstractStat):

    def result(self):
        if self.itt:
            return max(self.itt)
        else:
            return None


class AverageStat(AbstractStat):

    def result(self):
        if self.itt:
            return sum(self.itt) / len(self.itt)
        else:
            return None
