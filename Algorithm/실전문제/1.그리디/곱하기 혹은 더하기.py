data = input()

# 굳이 sort까진 필요없음
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else:
        result *= num

print(result)