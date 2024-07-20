def limiter(limit, unique, lookup):
    db_dict = dict()

    def wrapper(cls):
        def wrapper2(*args, **kwargs):
            obj = cls(*args, **kwargs)
            value = getattr(obj, unique)

            if value in db_dict:
                return db_dict[value]

            if len(db_dict) >= limit:
                if lookup == 'FIRST':
                    return tuple(db_dict.values())[0]
                elif lookup == 'LAST':
                    return tuple(db_dict.values())[-1]
            else:
                db_dict.setdefault(value, obj)

            return obj

        return wrapper2

    return wrapper