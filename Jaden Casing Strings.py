def to_jaden_case(string):
    answer = ''
    for i in range(len(string)):
        if i == 0 or string[i - 1] == ' ':
            answer += string[i].upper()
        else:
            answer += string[i].lower()
    return answer

# Something I saw in solutions
'''
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
'''
