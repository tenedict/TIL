n = int(input())

for _ in range(n):
    li = list(map(int,input().split()))
    li.sort(reverse = True)
    print(li[2])