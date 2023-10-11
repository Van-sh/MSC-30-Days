def nb_dig(n, d):
    squares = [str(i ** 2) for i in range(n + 1)]
    return sum([x.count(str(d)) for x in squares])