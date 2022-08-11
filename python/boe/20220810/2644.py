peo = int(input())
a, b = map(int,input().split())
n = int(input())
graph = [[] for _ in range(peo + 1)]

for _ in range(n):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]*(peo+1)

print(graph)
def dfs(start):
    stack = [start]
    visited[start] = True
    answer = 0
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                answer += 1
                print(adj,'0000000')
                print(answer)
                if b not in graph[cur]:
                    if len(graph[cur]) > 2:
                        answer -= (len(graph[cur]) - 2)
                if adj == b:
                    print(answer)
                visited[adj] = True
                stack.append(adj)
                
                
           


dfs(a)
               
print(a)