import sys

sys.stdin = open('10546.txt')

n = int(input())

player = []
for i in range(n):
    player += input().split()

finish = []

for j in range(n-1):
    finish += input().split()

gg = player - finish

print(gg)