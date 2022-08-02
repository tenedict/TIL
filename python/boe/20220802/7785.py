
n = int(input())


com = []
for i in range(n):
    a,b = (input().split())
    if b == 'enter':
        com.append(a)
    else:
        com.remove(a)


com.sort(reverse = True)
for j in com:
    print(j)