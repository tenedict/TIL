n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
total = 0
print(graph)
#인접리스트 만들기
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1,6):
    