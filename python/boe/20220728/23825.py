n, m = map(int,input().split())

if n > m:
    ans = m//2
elif m >= n:
    ans = n//2


print(ans)