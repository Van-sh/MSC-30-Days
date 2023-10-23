def distinct(seq):
    seen = set()
    i = 0
    while i < len(seq):
        if seq[i] in seen:
            del seq[i]
        else:
            seen.add(seq[i])
            i += 1
    return seq