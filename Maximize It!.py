from itertools import product

K, M = map(int, input().split())


lst = []

for _ in range(K):
    N, *arr = map(int, input().split())
    
    lst.append(arr)

max_val = 0

for case in product(*lst):
    result = sum([x ** 2 for x in case]) % M
    if result > max_val:
        max_val = result

print(max_val)