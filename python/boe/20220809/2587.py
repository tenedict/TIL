li = []
for _ in range(5):
    n = int(input())
    li.append(n)

li.sort()
print(int(sum(li)/5))
print(li[2])
