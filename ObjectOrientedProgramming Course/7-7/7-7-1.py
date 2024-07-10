class USADate:

    def __init__(self, year, month, date1):
        from datetime import date

        self.db = date(year, month, date1)

    def format(self):
        from datetime import date
        return f'{date.strftime(self.db, '%m-%d-%Y')}'

    def iso_format(self):
        from datetime import date
        return f'{date.strftime(self.db, '%Y-%m-%d')}'


class ItalianDate:

    def __init__(self, year, month, date1):
        from datetime import date

        self.db = date(year, month, date1)

    def format(self):
        from datetime import date
        return f'{date.strftime(self.db, '%d/%m/%Y')}'

    def iso_format(self):
        from datetime import date
        return f'{date.strftime(self.db, '%Y-%m-%d')}'


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())