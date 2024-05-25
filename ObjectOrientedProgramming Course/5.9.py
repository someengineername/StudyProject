def hash_function(obj):
    temp_obj = str(obj)
    temp1 = 0

    if len(temp_obj) % 2 == 0:

        l_mark = 0
        r_mark = len(temp_obj) - 1

        while l_mark < r_mark:
            temp1 += ord(temp_obj[l_mark]) * ord(temp_obj[r_mark])
            l_mark += 1
            r_mark -= 1

    else:
        l_mark = 0
        r_mark = len(temp_obj) - 1

        while l_mark != r_mark:
            temp1 += ord(temp_obj[l_mark]) * ord(temp_obj[r_mark])
            l_mark += 1
            r_mark -= 1

        temp1 += ord(temp_obj[len(temp_obj) // 2])

    temp2 = 0

    for pos, char in enumerate(temp_obj):
        if pos % 2 == 0:
            temp_sign = 1
        else:
            temp_sign = - 1
        temp2 += ord(temp_obj[pos]) * (pos + 1) * temp_sign

    return (temp1 * temp2) % 123456791


print(hash_function(12345))
