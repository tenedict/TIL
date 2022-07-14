#9번 문제 득표수 구하기

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

s = 0
for i in students:
    if i == '이영희':
        s +=1
    else:
        continue
print(s)
