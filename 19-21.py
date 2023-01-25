def f(s, c, m):
    if s >= 1000:
        return c % 2 == m % 2
    if c > m:
        return 0
    a = [f(s + 100, c + 1, m), f(s * 2, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)


for s in range(1, 1000):
    m = 4
    if f(s, 0, m):
        print(s, m)

