def accum(s):
    return '-'.join([(i * e).capitalize() for i, e in enumerate(s, 1)])
