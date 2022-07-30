n = input()
word = n.upper()

alp = {}
answer = ()
for i in word:
    if i not in alp:
        alp[i] = 1
    elif i in alp:
        alp[i] += 1

# print(alp)
ze = 0
for k,v in alp.items():
    if v > ze:
        ze = v
        answer = k
    elif v == ze:
        ze = v
        answer = '?'
    else:
        continue
print(answer)   
