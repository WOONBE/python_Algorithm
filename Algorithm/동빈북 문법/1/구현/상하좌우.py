n = int(input())
x, y = 1, 1  #입력
plans = input().split()

dx = [0,0,-1,1] #이 부분 햇갈리면 책에 좌표 다시 확인, 좌표때문에 잠깐 헤맴
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):  #왜 len(move_types)가 안에 들어가야 하나? 안에 n을 넣으려면 위에 plan에 처리해야함 근데 굳이?
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny<1 or nx > n or ny > n: #예외 처리
        continue
    x,y = nx, ny

print(x,y)




