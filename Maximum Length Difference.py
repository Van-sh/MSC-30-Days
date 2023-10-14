def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    al1 = [len(x) for x in a1]
    al2 = [len(x) for x in a2]
    return max(abs(max(al1) - min(al2)), abs(min(al1) - max(al2)))