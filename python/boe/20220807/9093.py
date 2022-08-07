n = int(input())

for i in range(n):
    li = list(input().split())
    for j in li:
       print(j[::-1],end=' ')
    print('')