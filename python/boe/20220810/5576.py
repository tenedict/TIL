w = []
k = []


for _ in range(10):
    n = int(input())
    w.append(n)

for _ in range(10):
    n = int(input())
    k.append(n)

top3w = []
for i in w:
    if len(top3w) < 3:
        top3w.append(i)
    elif len(top3w) == 3:
        top3w.sort(reverse = True)
        if i > top3w[2]:
            top3w.pop()
            top3w.append(i)


top3k = []
for i in k:
    if len(top3k) < 3:
        top3k.append(i)
    elif len(top3k) == 3:
        top3k.sort(reverse = True)
        if i > top3k[2]:
            top3k.pop()
            top3k.append(i)
print(sum(top3w),sum(top3k))