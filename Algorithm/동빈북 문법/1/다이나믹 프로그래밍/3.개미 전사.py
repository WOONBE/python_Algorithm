n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i-2] + array[i])

print(d[n-1])






















# n = int(input())
#
# d = []
#
# k = d.append(list(map(int, input().split())))
#
#
# result1 = 0
# result2 = 0
#
# for i in range(2, n+1, 2):
#     d[i] = max(d[i - 1], d[i])
#     result1 += d[i]
#
# for i in range(1, n+1, 2):
#     d[i] = max(d[i-1], d[i])
#     result2 += d[i]
#
# result3 = max(result1, result2)
#
# print(result3)



