#직접 구현
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k): # 원래는 역으로 계산하는 식으로 했는데 예외가 많아서 그냥 처음부터 시작, (0,k,1)이 결국 k랑 같다
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break


print(sum(a))




