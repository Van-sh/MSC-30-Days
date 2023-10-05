A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    B = set(map(int, input().split()))
    if not (A.issuperset(B) and len(A) > len(B)):
        print(False)
        break
else:
    print(True)
