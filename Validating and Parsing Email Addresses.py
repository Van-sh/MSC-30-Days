import email.utils
import re

n = int(input())
for _ in range(n):
    em = email.utils.parseaddr(input())
    if re.fullmatch(r'(?=[a-zA-Z])[0-9a-zA-Z\-_\.]*@[a-zA-Z]*\.[a-zA-Z]{1,3}', em[1]) is not None:
        print(email.utils.formataddr(em))