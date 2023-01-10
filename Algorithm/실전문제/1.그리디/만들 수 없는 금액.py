n = int(input())
k = list(map(int, input().split()))
k.sort()


target = 1

for x in k:
    if target < x:
        break
    target += x

print(target)


