input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1  #이부분이 햇갈림(알파벳을 수로 변환), 반대는 chr

steps = [(-2,-1),(-1,-2),(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2)]  #모든 경로 추가

result = 0
for step in steps:

    next_row = row + step[0]      #
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8: #이 부분 설정이 느릴수도 있음
        result += 1

print(result)