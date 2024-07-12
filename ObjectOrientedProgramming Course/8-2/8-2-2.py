from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, str1) -> str:
        return dict(zip(Seasons, ['зима', 'весна', 'лето', 'осень']))[self] if str1 == 'ru' else \
            dict(zip(Seasons, ['winter', 'spring', 'summer', 'fall']))[self]