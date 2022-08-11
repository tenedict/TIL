n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
total = 0
#인접리스트 만들기
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [False]* (n+1)

def dfs(start):
    stack = [start]
    visited[start]= True

    while stack:
        cur = stack.pop()
     

        for adj in graph[cur]:
           
            if not visited[adj]:
                
                visited[adj] = True
                stack.append(adj)

answer = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        answer += 1

print(answer)