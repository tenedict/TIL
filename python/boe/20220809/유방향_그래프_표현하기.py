adj=[
    [1,2],
    [2,5],
    [5,1],
    [3,4],
    [4,6],
]

matrix = [[0]*7 for _ in range(7)]

for edge in adj:
    v1, v2 = edge[0],edge[1]
    matrix[v1][v2] = 1
  
print(matrix)

li = [[] for _ in range(7)]

for edge in adj:
    v1, v2 = edge[0],edge[1]
    li[v1].append(v2)
    
print(li)