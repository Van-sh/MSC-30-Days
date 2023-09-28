M = int(input())
a = set(map(int, input().split()))

N = int(input())
b = set(map(int, input().split()))

print(*sorted(a.symmetric_difference(b)), sep='\n')
