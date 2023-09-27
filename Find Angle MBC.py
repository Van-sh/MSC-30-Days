import math

DEGREE_SYMBOL = u'\N{DEGREE SIGN}'

ab = int(input())
bc = int(input())

print(f'{round(math.degrees(math.atan(ab/bc)))}{DEGREE_SYMBOL}')
