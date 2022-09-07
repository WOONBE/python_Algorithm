#1.리스트 컴프리헨션(순서 ㅇ)
import heapq
import math
import sys
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import permutations, combinations

import counter as counter

array = [i for i in range(20) if i % 2 ==1]

#2차원 배열 초기화
n=3
m = 4
array = [[0] * m for _ in range(n)]
array.append(), \
array.sort(), \
array.reverse(), \
array.insert(위치,값), \
array.count(특정값), \
array.remove(특정값)
#append에 비해 insert는 느림

#2. 사전 자료형(순서 x)
data = dict() #로 초기화
data['사과'] = 'Apple'
key_list = data.keys()
value_list = data.values()

#각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

#3. 집합 자료형(순서 x)
data = set([1,2,3,4,5])
data = {1,1,2,3,4}
print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합

add(값), update([5,6등 한번에 추가]), remove(특정값)

#4.입출력
#입력
n = int(input())
#공백으로 구분하여 입력
data = list(map(int, input().split()))
#빠르게 입력(많은 수를 받을때)
sys.stdin.readline().rstrip()

#출력
#+에서 변수선언하거나 , 로 연결
answer = 7
print(f"정답은 {answer}입니다")

#5.내장함수
input()
print()
sum() #안에 리스트
min()
max()
eval("(3+5) * 7") #계산식 들어오면 수식 계산
sorted() #안에 리스트
result = sorted([(),(),()], key = lambda x : x[1],reverse = True) #1번자리 값 기준으로 오름차순 정렬

#6.itertools
list = list(permutations(data,3)) #data에서 3개를 뽑는 순열, product쓰면 중복해서 뽑음
list = list(combinations(data,2)) #data에서 2개를 뽑는 조합,combinations_with_replacement는 중복해서 뽑음

#7. heapq (우선순위 큐시)
heapq.heappush()
heapq.heappop()

#8. bisect(이진 탐색 구현)
bisect_left(a, x) #정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
bisect_right(a,x) #정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음

#특정 범위에 속하는 원소의 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

#9.collections
deque #보통은 1 표시한것만 사용
deque.popleft() #첫번째 원소 삭제 1
deque.pop() #마지막 원소 제거
deque.appendleft(x) #첫번째에 x삽입
deque.append(x) #마지막에 삽입1

Counter

#10. math
math.factorial() #팩토리얼
math.sqrt() #제곱근
math.gcd() #최대 공약수
math.pi
math.e











