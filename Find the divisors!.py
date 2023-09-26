def divisors(integer):
    div = [x for x in range(2, integer // 2 + 1) if integer % x == 0]
    if len(div) == 0:
        return f'{integer} is prime'
    else:
        return div
