class RoundedInt(int):

    def __new__(cls, obj, even=True):

        if even:
            obj = obj + obj % 2

        else:
            obj = obj + (1 - obj % 2)

        instance = super().__new__(cls, obj)
        instance.even = even
        return instance

roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))