def sum_of_multiples(limit, multiples):
    result = []
    for num in multiples:
        if num:
            result += [number for number in range(num, limit, num)]
    return sum(set(result))
