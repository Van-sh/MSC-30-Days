def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a, b + 1):
        num = str(i)
        sum = 0
        for j in range(len(num)):
            sum += int(num[j]) ** (j + 1)
        if sum == i:
            result.append(i)
    return result
