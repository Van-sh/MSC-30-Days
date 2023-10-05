T = int(input())

for _ in range(T):
    len_A = int(input())
    A = set(map(int, input().split()))

    len_B = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
