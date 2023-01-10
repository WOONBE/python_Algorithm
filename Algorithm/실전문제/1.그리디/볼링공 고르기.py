n, m = map(int, input().split())
ball = list(map(int, input().split()))
# ball.sort()
# count = 0
#
# for i in range(1, len(ball) - 1):
#     for k in range(2, len(ball) - 1):
#         if ball[i] != ball[k]:
#             count += 1
#
# print(count)
array = [0] * 11

for x in ball:
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)



