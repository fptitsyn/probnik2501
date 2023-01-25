import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


@lru_cache()
def f(n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return 1 + f(n - 1)
    return f(n // 2)


c = 0
for i in range(1, 500_000_001):
    k = f(i)
    if k == 3:
        print(i)
        c += 1

print(c)