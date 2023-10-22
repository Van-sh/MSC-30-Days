import numpy



N, M, P = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
A = numpy.array(lst)
lst = [list(map(int, input().split())) for _ in range(M)]
B = numpy.array(lst)
print(numpy.concatenate((A, B), axis=0))