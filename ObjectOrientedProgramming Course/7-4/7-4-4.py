from collections import UserList


class AdvancedList(UserList):

    def join(self, spacer=' '):
        return spacer.join([str(i) for i in self.data])

    def map(self, defunc):
        self.data = AdvancedList([defunc(i) for i in self.data])

    def filter(self, defunc):
        self.data = AdvancedList(list(filter(defunc, self.data)))
