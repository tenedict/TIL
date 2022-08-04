import sys
n = int(sys.stdin.readline())

player = []
for i in range(n):
    player += sys.stdin.readline().split()

finish = []

for j in range(n-1):
    finish += sys.stdin.readline().split()

for u in player:
    if u not in finish:
        print(u,end='')
