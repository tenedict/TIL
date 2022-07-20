
n = int(input())

for r in range(1,n+1):
    a = list(map(int, input().split()))

    for i in a:
        if a[0]<i:
            a[0]=i
    print(f'#{r} {a[0]}')