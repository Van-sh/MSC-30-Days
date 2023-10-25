import numpy



N, M = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.mean(arr, axis=1), numpy.var(arr, axis=0), round(numpy.std(arr), 11), sep='\n')