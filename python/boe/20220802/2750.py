import heapq

n = int(input())
num = []


for i in range(1,n+1):
    heapq.heappush(num,i)


while num:
    print(heapq.heappop(num)[1])




print(num)