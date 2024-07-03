import datetime


class WeatherWarning:

    @staticmethod
    def rain():
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow():
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature():
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):

    @staticmethod
    def rain(date):
        print(datetime.date.strftime(date, '%d.%m.%Y'))
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow(date):
        print(datetime.date.strftime(date, '%d.%m.%Y'))
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature(date):
        print(datetime.date.strftime(date, '%d.%m.%Y'))
        print('Ожидается сильное понижение температуры')
