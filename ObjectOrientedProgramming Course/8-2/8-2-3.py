from enum import Enum
from datetime import date
from dateutil.relativedelta import relativedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:

    def __init__(self, today: date, weekday: Weekday, considering_today=False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today
        self.counter = 0

    def date(self):

        if self.today.weekday() != self.weekday.value:

            counter = 0
            temp_date = self.today
            while ...:
                temp_date += relativedelta(days=1)
                counter += 1

                if temp_date.weekday() == self.weekday.value:
                    self.counter = counter
                    break

            return temp_date


        else:

            # если учитываем "сегодня" и эти дни и так уже равны - то дельта (каунтер) == 0, и возвращаем "сегондя
            if self.considering_today and self.today.weekday() == self.weekday.value:
                self.counter = 0
                return self.today

            # если учитываем "сегодня" но эти дни не равны, то "отсчитываем от сегодняшней даты и идём
            # в бесконечность, пока не найдём weekday
            if not self.considering_today:
                counter = 0
                temp_date = self.today
                while ...:
                    temp_date += relativedelta(days=1)

                    counter += 1

                    if temp_date.weekday() == self.weekday.value:
                        self.counter = counter
                        break

                return temp_date

    def days_until(self):
        return self.counter
