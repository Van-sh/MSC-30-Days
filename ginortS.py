S = input()

print(''.join(sorted([x for x in S if x.islower()]) + sorted([x for x in S if x.isupper()]) + sorted([x for x in S if x.isdigit() and (int(x) % 2 != 0)]) + sorted([x for x in S if x.isdigit() and (int(x) % 2 == 0)])))
