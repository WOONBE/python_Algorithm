n = int(input())

count = 0
for i in range( n + 1):  #시간
    for j in range(60): #분
        for k in range(60): #초

            if '3' in str(i) + str(j) + str(k): #의 숫자중에 하나라도 3이 있으면 카운트 업
                count += 1

print(count)
