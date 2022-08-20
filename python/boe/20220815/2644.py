n = int(input())
a,b = map(int,input().split())
nn = int(input())
graph = [[] for _ in range(nn)]
for i in range(nn):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]*n
def bfs():
    sta = [start]
    visited[start] = True

    w
