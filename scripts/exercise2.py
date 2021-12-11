def staircase_d(n):
    cache = []
    if n == 1:
        cache.append(1)
        return 1
    elif n == 2:
        cache.append(2)
        return 2
    elif n == 3:
        cache.append(4)
        return 4
    else:
        cache.append(cache[-1] + cache[-2] + cache[-3])
        return cache[-1]
