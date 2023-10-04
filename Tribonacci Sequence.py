def tribonacci(signature, n):
    result = signature
    for i in range(n - 3):
        result.append(result[i] + result[i + 1] + result[i + 2])
    return result[:n]
