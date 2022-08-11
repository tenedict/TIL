
for i in range(1,4):
    n = input()
    li = []
    int_ = 0
    answer = 0
    for j in n:
        if j != int_:
            int_ = j
            answer = 1
            li.append(answer)
        else:
            answer += 1
            li.append(answer)

    print(max(li))