def f(x):
    if x <= -2:
        m = 1 - (x + 2) ** 2
        return m
    if -2 < x <= 2:
        m = - x / 2
        return m
    if 2 < x :
        m = (x - 2) ** 2 + 1
        return m
