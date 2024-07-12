from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        db_dict = {self.CONTINUE: 'информация ',
                   self.OK: 'успех',
                   self.USE_PROXY: 'перенаправление',
                   self.NOT_FOUND: 'ошибка клиента',
                   self.BAD_GATEWAY: 'ошибка сервера'}
        return db_dict[self]