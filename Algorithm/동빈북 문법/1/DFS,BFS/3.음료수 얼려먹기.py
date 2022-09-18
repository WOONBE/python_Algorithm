n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input()))) #split은 필요없음(공백이 없어서)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end='')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# visited = [False] * n

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #방문 x시 방문처리

    if graph[x][y] == 0:
        graph[x][y] = 1
        #상하좌우 탐색, 재귀함수

        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)





