n, m = map(int,input().split())

graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

#인접리스트 만들기
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v2):
    visited[v2]=True
    for i in graph[v2]:
        if not visited[i]:
            dfs(i)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result+=1
print(result)
