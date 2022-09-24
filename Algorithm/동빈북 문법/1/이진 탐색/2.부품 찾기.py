# 다른 풀이방식들도 참조


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


# 부품 목록
n = int(input())
array = list(map(int, input().split()))
array.sort()  # 사전에 정렬 실행

# 손님이 확인 요청한 품목 입력
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)

    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
