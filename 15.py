ans = []
for a in range(-500, 500):
    for x in range(500):
        for y in range(500):
            if not (((x * y) < a) or (x >= 16) or (x < (5 * y))):
                break
        if not (((x * y) < a) or (x >= 16) or (x < (5 * y))):
            break
    else:
        ans.append(a)
        
print(min(ans))