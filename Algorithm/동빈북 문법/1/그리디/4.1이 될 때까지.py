n, k = map(int,input().split())

#내가 풀이한 코드: 거의다 들어맞는데 예외가 걸려서 수정이 필요하다
count = 0
while True:
    if (n == 1):
        break
    elif (n % k == 0):
        n = n // k
        count += 1
    else:
        n = n-1
        count += 1


print(count)

#권장 정답
result = 0

#n이 k이상이면 k로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n>1:
    n -=1
    result += 1

print(result)



