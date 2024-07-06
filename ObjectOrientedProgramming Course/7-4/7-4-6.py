from collections import UserDict


class ValueDict(UserDict):

    def keys_of(self, value):
        temp_list = [[v, k] for k, v in self.data.items()]

        try:
            temp_list2 = [i[1] for i in list(filter(lambda x: x[0] == value, temp_list))]
            yield from temp_list2
        except:
            yield from []

    def key_of(self, value):
        temp_list = [[v, k] for k, v in self.data.items()]
        try:
            temp_list2 = list(filter(lambda x: x[0] == value, temp_list))
            return temp_list2[0][1]
        except:
            return None


valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))