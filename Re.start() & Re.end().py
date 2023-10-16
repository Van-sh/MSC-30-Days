import re

S = input()
k = input()

m = list(re.finditer(f'(?={re.escape(k)})', S))
if m == []:
    print((-1, -1))
else:
    print(*[(x.start(), x.start() + len(k) - 1) for x in m], sep='\n')