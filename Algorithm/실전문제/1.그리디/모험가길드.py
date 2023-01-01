n = input()
k = list(map(int,input().split()))

k.sort()

result = 0   # 그룹수
count = 0   # 그룹의 모험가 수

for i in k:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
