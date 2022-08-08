cards, num = map(int,input().split())

nuli = list(map(int,input().split()))


answer = []
for i in range(cards):
    for j in range(cards):
            if j != i:
                for h in range(cards):
                    if h != i and h!= j:
                        sum_ = nuli[i] + nuli[j] + nuli[h]
                        
                        if sum_ <= num:
                            answer.append(sum_)
print(max(answer))

