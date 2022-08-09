li = []


s = input().replace('\n', '').replace(' ','')


for i in s:
    li.append(i)

li.sort()
print(li)