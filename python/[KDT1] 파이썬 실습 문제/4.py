#4번 문제 곱 구하기

n = int(input())

s = 1
for i in range(1,n+1):
    s *= i
print(s)