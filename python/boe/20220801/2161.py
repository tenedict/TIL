from collections import deque


n = int(input())
list_ = deque(range(1,n+1))

while len(list_) > 1:
    print(list_.popleft(), end=' ')
    list_.append(list_.popleft())

print(list_[0])

