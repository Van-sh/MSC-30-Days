N, X = map(int, input().split())

marks = []

for _ in range(X):
    marks.append(list(map(float, input().split())))

print(*[sum(student) / X for student in zip(*marks)], sep="\n")