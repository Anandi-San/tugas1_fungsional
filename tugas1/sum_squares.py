def sum_squares(x):
    y = len(x)
    res = [(y * (y + 1) * (2 * y + 1)) // 6]
    return sum(res)

print(sum_squares([1, 2, 3]))