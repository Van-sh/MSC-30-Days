def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    result = ''
    for i in range(n // 2 + 1):
        result += ('*' * ((i * 2) + 1)).rjust(n // 2 + i + 1) + '\n'
    for i in range(n // 2):
        result += ('*' * (n - ((i + 1) * 2))).rjust(n - i - 1) + '\n'
    
    return result
