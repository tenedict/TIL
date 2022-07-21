n = input()
n = int(n)

for i in range(1,n+1):
    a, b, c, d = map(int, input().split())

    if a + c < 12:
        g = a + c
    else:
        g = a + c -12

    if b + d < 60:
        gg = b + d
    else:
        gg = b + d - 60
        g += 1

    print(f'#{i} {g} {gg}')