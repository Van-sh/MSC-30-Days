import numpy



N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
A = numpy.array(lst)
lst = [list(map(int, input().split())) for _ in range(N)]
B = numpy.array(lst)

print(A + B, A - B, A * B, A // B, A % B, A ** B, sep='\n')