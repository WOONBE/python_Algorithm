n, m = map(int, input().split()) #입력
#작은수 3개 뽑아서 걔네끼리 비교해서 가장 큰수를 뽑아낸다

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data) #가장 작은수 추출
    result = max(result, min_value)  #비교해서 max찾음

print(result)


