def jsonattr(json_filename):
    def decorator(cls):
        import json

        with open(json_filename, 'r', encoding='UTF-8') as file:
            values = json.load(file)

            for k, v in values.items():
                setattr(cls, k, v)

        return cls

    return decorator
