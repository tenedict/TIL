#8번 문제 두번째로 큰 수 구하기

numbers = [10000, 432, 100,1,2 ,2 ,4,6]

p = numbers[0]

for i in numbers:
    if i > p :
        p = i
    else:
        continue

numbers.remove(p)

o = numbers[0]
for i in numbers:
    if i > o :
        o = i
    else:
        continue
    
print(o)
