n = int(input())
answer = 0
g = int(input())
for _ in range(g):
    a,b = map(int,input().split())
    answer += (a*b)

if answer == n:
    print('Yes')
else:
    print('No')