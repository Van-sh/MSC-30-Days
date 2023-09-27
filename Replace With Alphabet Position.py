def alphabet_position(text):
    return ' '.join([str(ord(x) & 31) for x in text if x.isalpha()])
