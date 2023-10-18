import re

pattern = re.compile(r'^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*\d){3,})[a-zA-Z0-9]{10}$')

T = int(input())
for i in range(T):
    uid = input()
    m = pattern.match(uid)
    print('Valid' if m is not None else 'Invalid')