import numpy



dimensions = tuple(map(int, input().split()))
print(numpy.zeros(dimensions, dtype=int), numpy.ones(dimensions, dtype=int), sep='\n')