x = int(input())

d = [0] * 30001

# 끝에 +1은 호출횟수를 구하기 위함
# 그냥 계산식을 테이블에 다 넣어줬다 생각하면 된다(중복 회피)
# 계산들을 비교해서 계속해서 최솟값 찾아냄

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i //3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])


# 내 풀이(특정 수에서 예외 발생)
# count = 0
# while True:
#     if (n == 1):
#         break
#     elif (n % 5 != 0):
#         n = n-1
#         count += 1
#     else:
#         n = n // 5
#         count += 1
# while n < 5:
#     if (n == 1):
#         break
#     elif (n % 3 != 0):
#         n = n-1
#         count += 1
#     else:
#         n = n //3
#         count += 1
# while n < 3:
#     if (n == 1):
#         break
#     elif (n % 2!= 0):
#         n = n-1
#         count += 1
#     else:
#         n = n //2
#         count += 1
#
#
# print(count)




