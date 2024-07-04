class FuzzyString(str):

    def __eq__(self, other):  # ==
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() == str(other).lower()
        return NotImplemented

    def __ne__(self, other):  # !=
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() != str(other).lower()
        return NotImplemented

    def __lt__(self, other):  # <
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() < str(other).lower()
        return NotImplemented

    def __gt__(self, other):  # >
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() > str(other).lower()
        return NotImplemented

    def __le__(self, other):  # <=
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() <= str(other).lower()
        return NotImplemented

    def __ge__(self, other):  # >=
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(self).lower() >= str(other).lower()
        return NotImplemented

    def __contains__(self, other):  # other in self
        if isinstance(other, str) or isinstance(other, FuzzyString):
            return str(other).lower() in str(self).lower()
        return NotImplemented
