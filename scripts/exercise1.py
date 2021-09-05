def staircase_r(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase_r(n - 1) + staircase_r(n - 2) + staircase_r(n - 3)
