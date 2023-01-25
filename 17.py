f = open("17.txt")

a = [int(i) for i in f]

min17 = 10001
c = 0
for i in a:
    if i % 17 == 0:
        c += 1
        min17 = min(min17, i)

b = []

for i in range(len(a) - 1):
    if (a[i] % min17 == 0) or (a[i + 1] % min17) == 0:
        b.append(a[i] + a[i + 1])

print(c)
print(len(b), max(b))
