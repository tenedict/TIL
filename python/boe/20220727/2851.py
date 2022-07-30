mush = []
score = 0
for i in range(10):
    mush.append(int(input()))
for j in mush:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
    else:
        continue
print(score)