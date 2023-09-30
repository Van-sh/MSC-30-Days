from collections import deque

d = deque()

N = int(input())

for _ in range(N):
    command, *arg = input().split()
    getattr(d, command)(*map(int, arg))

print(*d)
