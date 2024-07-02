from itertools import cycle


def limited_hash(left, right, hash_function=hash):
    def inside_func(input_value):
        cycler = cycle(list(range(left, right + 1)))
        raw_hash = hash_function(input_value)

        if left <= raw_hash <= right:

            return raw_hash

        elif raw_hash < left:

            list1 = list(range(left, right + 1))
            raw_position = left - raw_hash
            return list1[-(raw_position % len(list1))]

        elif raw_hash > right:

            counter = raw_hash - right
            answer = 0

            for i in cycler:
                if counter > 0:
                    answer = i
                    counter -= 1
                else:
                    break

            return answer

    return inside_func
