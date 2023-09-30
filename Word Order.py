from collections import OrderedDict

words = OrderedDict()

n = int(input())

for _ in range(n):
    x = input()
    
    if x not in words:
        words[x] = 1
    else:
        words[x] += 1

print(len(words))
print(*[words[word] for word in words])
