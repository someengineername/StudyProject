from string import Template


class DeltaTemplate(Template):
    delimiter = "%"


class Lecture:

    def __init__(self, topic, start_time, duration):
        from datetime import datetime as dt
        from datetime import timedelta as td

        self.duration_cache = duration

        self.topic = topic
        self.start_time = dt.strptime(start_time, '%H:%M')
        self.duration_in_minutes = (dt.strptime(duration, '%H:%M').hour * 60 +
                                    dt.strptime(duration, '%H:%M').minute)
        self.end_time = self.start_time + td(minutes=self.duration_in_minutes)

    def __repr__(self):
        return f'({self.topic}/{self.start_time}/{self.end_time})'


class Conference:

    def __init__(self):
        self.db = []

    def add(self, obj: Lecture):

        if self.db:

            for pos in self.db:
                delta1 = 0

                if pos.start_time > obj.start_time:
                    delta1 = (pos.start_time - obj.end_time).days
                elif pos.start_time < obj.start_time:
                    delta1 = (obj.start_time - pos.end_time).days
                elif pos.start_time == obj.start_time:
                    delta1 = -1

                if delta1 >= 0:
                    pass
                else:
                    raise ValueError('Провести выступление в это время невозможно')

            self.db.append(obj)
            self.db.sort(key=lambda x: x.start_time)

        # if db is empty
        else:
            self.db.append(obj)
            self.db.sort(key=lambda x: x.start_time)

    def __repr__(self):
        return f'{self.db}'

    def total(self):
        from datetime import timedelta as td
        bake1 = td(minutes=sum(i.duration_in_minutes for i in self.db))
        return self.strfdelta(bake1, '%H:%M')

    def longest_lecture(self):
        return max(self.db, key=lambda x: x.duration_in_minutes).duration_cache

    def longest_break(self):
        from datetime import timedelta as td

        result = td()

        for num in range(len(self.db) - 1):
            temp_td = self.db[num + 1].start_time - self.db[num].end_time
            if temp_td > result:
                result = temp_td

        return self.strfdelta(result, '%H:%M')

    @staticmethod
    def strfdelta(tdelta, fmt):
        d = {"D": tdelta.days}
        hours, rem = divmod(tdelta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        d["H"] = '{:02d}'.format(hours)
        d["M"] = '{:02d}'.format(minutes)
        d["S"] = '{:02d}'.format(seconds)
        t = DeltaTemplate(fmt)
        return t.substitute(**d)
