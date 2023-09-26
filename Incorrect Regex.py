import re

T = int(input())

for _ in range(T):
    string = input()
    try:
        pattern = re.compile(string)
        print(True)
    except:
        print(False)
