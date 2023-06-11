def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) == len(strand_b):
        for ind in range(len(strand_a)):
            if strand_b[ind] != strand_a[ind]:
                count += 1
    else:
        raise ValueError("Strands must be of equal length.")
    return count
