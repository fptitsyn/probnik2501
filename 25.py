def d(n):
    a = set()
    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            s = str(i)
            c = 0
            for j in s:
                if int(j) % 2 == 1:
                    c += 1
            if c == len(s):
                a.add(i)
            s = str(n // i)
            c = 0
            for j in s:
                if int(j) % 2 == 1:
                    c += 1
            if c == len(s):
                a.add(n // i)

    if len(a) >= 5:
        b = sorted(a)
        return b[::-1]
    else:
        return 0


a = []
for n in range(300_000_000, 1, -1):
    k = d(n)
    if k != 0:
        a.append((k[4], len(k)))
    if len(a) == 5:
        break

print(a[::-1])

