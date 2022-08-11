matrix = [[0,0,0,0,0,0,0,0] for _ in range(8)]

a, b, c = input().split()
king = list(a)
stone = list(b)
li = [king,stone]
for u in li:
    if u[0] == 'A':
        u[0] = 0
    if u[0] == 'B':
        u[0] = 1
    if u[0] == 'C':
        u[0] = 2
    if u[0] == 'D':
        u[0] = 3
    if u[0] == 'E':
        u[0] = 4
    if u[0] == 'F':
        u[0] = 5
    if u[0] == 'G':
        u[0] = 6
    if u[0] == 'H':
        u[0] = 7
print(king)
print(stone)

matrix[king[0]][int(king[1])-1] = 1
matrix[stone[0]][int(stone[1])-1] = 2
print(matrix)

for i in range(c):
    n = input()
    if n == 'R':
        