n = int(input())

player = []
for i in range(n):
    player += input().split()

finish = []

for j in range(n-1):
    finish += input().split()

for k in finish:
    player.remove(k)

print(player[0])