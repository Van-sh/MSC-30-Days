T = int(input())

for _ in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except Exception as err:
        print(f'Error Code: {err}')
