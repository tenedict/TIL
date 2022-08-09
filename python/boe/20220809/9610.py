n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axts = 0


for _ in range(n):
    a, b = map(int,input().split())
    if a > 0 and b >0:
        q1 += 1
    if a >0 and b < 0:
        q4 += 1
    if a < 0 and b > 0:
        q2 += 1
    if a <0 and b<0:
        q3 += 1
    if a == 0 or b == 0:
        axts += 1
    
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axts}')
