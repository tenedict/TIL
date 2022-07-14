#10번문제 5의 개수 구하기

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

s =0
for i in numbers:
    if i == 5:
        s +=1
    else:
        continue

print(s)