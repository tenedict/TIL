import sys
a, b = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(a):
    line = list(sys.stdin.readline().split())
    matrix.append(line)

n = int(input())
for i in range(n):
    ii, jj, xx ,yy = map(int,input().split())
    sum_ = 0
    for j in range(ii-1,xx):
        for k in range(jj-1,yy):
          sum_ += int(matrix[j][k])
    print(sum_)