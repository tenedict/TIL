n = int(input())
c = 665
count = 0
li = []
while True:
    c += 1
    if '666' in str(c):
        li.append(c)
    else:
        continue
    if len(li) == n:
        break
print(li.pop())

    
