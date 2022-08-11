n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
total = 0

#인접리스트 만들기
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)

visited = [False]* (n+1)

def dfs(start):
    stack = [start]
    visited[start]= True

    while stack:
        cur = stack.pop()
        print('*#*#*#')
        print(cur)
        print('-----')

        for adj in graph[cur]:
            print(visited)
            if not visited[adj]:
                print(adj)
                visited[adj] = True
                stack.append(adj)
dfs(1)

print(sum(visited)-1)