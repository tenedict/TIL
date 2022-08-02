n = int(input())


for _ in range(n):
    r, e, c = map(int,input().split())

    if e-r > c:
        print('advertise')
    elif e-r == c:
        print('does not matter')
    else:
        print('do not advertise')