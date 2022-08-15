import sys
li = [0]*26

s = sys.stdin.read().replace('\n', '').replace(' ','')

for i in s:
    li[ord(i)-97] += 1

for j in range(26):
    if li[j] == max(li):
        print(chr(97+j), end ='')
