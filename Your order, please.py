import re

def order(sentence):
    pattern = re.compile('\d')
    words = sentence.split()
    return ' '.join(sorted(words, key=lambda word: pattern.search(word)[0]))
