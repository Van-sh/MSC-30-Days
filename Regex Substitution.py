import re

N = int(input())

substitutions = {'||': 'or', '&&': 'and'}

text = '\n'.join([input() for _ in range(N)])

print(re.sub(r'(?<= )(\|\||&&)(?= )', lambda x: substitutions[x[0]], text))