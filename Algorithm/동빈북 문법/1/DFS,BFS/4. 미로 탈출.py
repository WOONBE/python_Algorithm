from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input()))) #입력

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상,하,좌,우 정의

def bfs(x, y): #bfs 함수 설정

    queue = deque()
    queue.append((x,y))
    #큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4): #4방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]

            #예외 처리
            if nx < 0 or ny > 0 or nx >= n or ny >= m:
                continue

            #괴물은 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] == graph[x][y] + 1
                queue.append((nx, ny))
                #마지막 좌표까지의 거리 반환
        return graph[n - 1][m - 1]


print(bfs(0, 0))