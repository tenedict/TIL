#12번 문제 문자열 조작하기

n = input()

for i in n:
    if i == 'a':
        continue
    else:
        print(i,end='')

#다른 방법
#input = 'apple'

#while 'a' in input:
#    input = input.replace('a', '')

#print(input)