nan = []

for _ in range(9):
    n =int(input())
    nan.append(n)
alll = sum(nan)

for i in range(9):
    for j in range(9):
        if j != i:
            if alll -nan[i] -nan[j] == 100:
                a,b = i,j
                break
nan.remove(nan[a])
nan.remove(nan[b])
nan.sort()
for h in nan:
    print(h)

