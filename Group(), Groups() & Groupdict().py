import re

pattern = r"([a-zA-Z0-9])\1{1,}"

S = input()

m = re.search(pattern, S)

print(-1 if m is None else m.group(1))
