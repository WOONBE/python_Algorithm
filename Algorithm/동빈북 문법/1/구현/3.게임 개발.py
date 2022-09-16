n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] #리스트 컴프리헨션

x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 방문한 곳은 1처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #북,동,남,서
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:

    turn_left() #도는건 필수
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전 후 정면에 가보지 않은 칸이 있으면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    #회전 후 정면에 가보지 않은 칸이 없거나 바다일때
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0: #1로는 표시 안해도 된다(이미 해놓은 상태기 때문에)
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)





