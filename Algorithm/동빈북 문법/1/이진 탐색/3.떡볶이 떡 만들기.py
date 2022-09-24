n, m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족할 경우
    if total < m:
        end = mid - 1
    # 떡의 양이 충분할 경우 total > m
    else:
        result = mid
        start = mid + 1

print(result)





