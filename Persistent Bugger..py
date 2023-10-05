def persistence(n):
    result = 0
    while n > 9:
        digits = list(map(int, str(n)))
        n = 1
        for digit in digits:
            n *= digit
        result += 1
    return result
