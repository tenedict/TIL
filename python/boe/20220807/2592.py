su = []
for _ in range(10):
    n = int(input())
    su.append(n)

maxx= 1
answer = su[0]
for i in su:
    susu = su.count(i)
    if susu > maxx:
        maxx = susu
        answer = i

print(int(sum(su)/10))
print(answer)

