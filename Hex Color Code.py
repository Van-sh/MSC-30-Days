import re

pattern = re.compile(r'(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))(?!\s*(?:\n|{))\b')

N = int(input())

css = '\n'.join([input() for _ in range(N)])

m = pattern.findall(css)

print(*m, sep='\n')