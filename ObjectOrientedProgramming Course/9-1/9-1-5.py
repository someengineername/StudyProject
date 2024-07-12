import re


class DomainException(Exception):
    pass


class Domain:

    def __init__(self, obj=None):
        self.domain = ''

        domain_pattern = r'[a-zA-Z]{1,}\.[a-zA-Z]{2,}'

        if re.fullmatch(domain_pattern, obj):
            self.domain = obj
        else:
            raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_url(cls, obj: str):

        from_irl_pattern = r'(https\:\/\/|http\:\/\/)([a-zA-Z]{1,}\.[a-zA-Z]{2,})'

        if re.fullmatch(from_irl_pattern, obj):
            a = re.search(from_irl_pattern, obj)
            return cls(a.group(2))
        else:
            raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_email(cls, obj: str):

        from_irl_pattern = r'([a-zA-Z]{1,}@)([a-zA-Z]{1,}\.[a-zA-Z]{2,})'

        if re.fullmatch(from_irl_pattern, obj):
            a = re.search(from_irl_pattern, obj)
            return cls(a.group(2))
        else:
            raise DomainException('Недопустимый домен, url или email')

    def __str__(self):
        return self.domain
