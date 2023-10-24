def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)