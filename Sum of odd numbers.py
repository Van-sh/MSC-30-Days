def row_sum_odd_numbers(n):
    n_row_first_num = 1 + ((n - 1) * n)
    return n * ((2 * n_row_first_num) + (n - 1) * 2) // 2
