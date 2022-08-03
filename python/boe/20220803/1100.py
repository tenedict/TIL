matrix = []
for _ in range(8):
    line = list(input())
    matrix.append(line)


count = 0
for i in (0,2,4,6):
    for j in (0,2,4,6):
        if matrix[i][j] == 'F':
            count += 1

for i in (1,3,5,7):
    for j in (1,3,5,7):
        if matrix[i][j] == 'F':
            count += 1

print(count)