n = int(input())
c = list(map(int, input().split()))
max = 0

for i in range(n):
    if(c[i] == max%3):
        max+=1

print(max)

