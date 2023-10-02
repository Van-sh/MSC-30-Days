from collections import Counter



if __name__ == '__main__':
    s = input()
    letter_counter = Counter(sorted(s))
    result = letter_counter.most_common(3)
    for e in result:
        print(*e)
