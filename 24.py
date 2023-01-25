f = open("24.txt")

a = f.read()

k = 1
kmax = 1
knum = 0
currentk = 0

for i in range(len(a) - 1):
    if ord(a[i]) > ord(a[i + 1]):
        k += 1
        if k > kmax:
            kmax = k
            knum = currentk + 1
    else:
        k = 1
        currentk = i + 1

print(knum)
