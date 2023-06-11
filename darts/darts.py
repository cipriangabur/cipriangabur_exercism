dict_range = {
    (25, 100): 1,
    (1, 25): 5,
    (0, 1): 10
}


def is_between(value, interval):
    return interval[0] < value <= interval[1]


def score(x, y):
    if x == y == 0:
        return 10
    else:
        for key, data in dict_range.items():
            if key[0] < (x - 0) ** 2 + (y - 0) ** 2 <= key[1]:
                return data
        return 0
