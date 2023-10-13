import re

pattern = re.compile(r'\b(?=[789])\d{10}\b')

N = int(input())

for _ in range(N):
    print('YES' if bool(pattern.match(input())) else 'NO')