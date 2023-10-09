import re

pattern = re.compile(r'((?:\+|-)?\d*\.\d+)')

T = int(input())

for _ in range(T):
    N = input()
    print(re.fullmatch(pattern, N) is not None)
