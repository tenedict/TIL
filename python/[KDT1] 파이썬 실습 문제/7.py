#7번 문제 최솟값 구하기

numbers = [0, 20, -100,324234]

p = numbers[0]
for i in numbers:
    if i < p:
        p = i
    else:
        continue
print(p)