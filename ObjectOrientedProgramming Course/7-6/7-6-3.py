def get_method_owner(cls, method):
    answer = []

    for pos in cls.mro():
        if method in pos.__dict__:
            answer.append(pos)

    if answer:
        return answer[0]
    else:
        return None
