f = open("26.txt")

a = [i.strip().split() for i in f.readlines()][1:]

for i in range(len(a)):
    for j in range(2):
        a[i][j] = int(a[i][j])

a = sorted(a)

c = 0
maxs = 0
maxnum = 0

b = []
for i in range(len(a) - 1):
    if a[i][0] == a[i + 1][0]:
        b.append(a[i])
    else:
        b.append(a[i])
        print(len(b))
        s = 0
        rest = 0
        for j in range(len(b)):
            if (s + b[j][1]) <= 500:
                s += b[j][1]
            else:
                c += 1
                rest += b[j][1]
                if rest > maxs:
                    maxs = rest
                    maxnum = b[j][0]
        b = []

print(c, maxnum)
