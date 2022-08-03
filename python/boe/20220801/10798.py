matrix = []

for _ in range(5):
    n = list(input())
    matrix.append(n)



aaa = []

for j in range(0,15):
    for k in matrix:
        if len(k) > j:
            aaa.append(k[j])
        else:
            continue

for u in aaa:
    print(u, end='')
