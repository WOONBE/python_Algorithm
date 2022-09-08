n, m, k = map(int, input().split()) #입력., 3개까진 굳이 앞에 리스트 안붙여도 됨
data = list(map(int, input().split())) #리스트 입력
#가장 큰 수와 두번째로 큰 수만 얻으면 된다(그리디)
# data를 sort해줘야하는것 유의하고 간다.

data.sort()
first = data[n-1] #n번째 수가 n-1로 표시되므로 빼줘야함
second = data[n-2]

#1번풀이
result = 0

while True:
    for i in range(k):  #가장 큰수를 k번 더하고, 2번째를 한번 더하고 다시 반복
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

#2번풀이

#가장 큰 수가 더해지는 횟수 계산
count = int(m/ (k+1)) * k #1은 second 갯수임
count += m % (k+1) #몫이 넘어갈때

result = 0
result += (count) * first #count 만큼 더함
result += (m-count) * second #count에서 남는만큼 더함

print(result)

















