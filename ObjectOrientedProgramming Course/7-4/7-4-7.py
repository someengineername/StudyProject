from collections import UserDict


class BirthdayDict(UserDict):

    def __setitem__(self, key, value):

        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        else:
            self.data[key] = value
