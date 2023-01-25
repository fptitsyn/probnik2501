f = open("27b.txt")

a = [i.strip().split() for i in f.readlines()][1:]

for i in range(len(a)):
    for j in range(2):
        a[i][j] = int(a[i][j])

b = []
for i in a:
    if i[0] % 2 == 1:
        b.append(i)

maxs = 0
for k in range(0, len(b)):
    c = [b[k]]
    for i in range(k + 1, 9):
        c.append(b[i])
        bigs = 0
        smalls = 0
        for j in c:
            bigs += max(j)
            smalls += min(j)
        if bigs % 2 == 1 and smalls % 2 == 0:
            maxs = max(maxs, bigs + smalls)


print(maxs)