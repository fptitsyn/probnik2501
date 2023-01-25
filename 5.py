def f(n):
    b = bin(n)[2:]
    for _ in range(2):
        s = b.count("1")
        b += str(s % 2)
    return int(b, 2)


ans = []
for n in range(100):
    r = f(n)
    if r > 43:
        ans.append(r)

print(min(ans))
