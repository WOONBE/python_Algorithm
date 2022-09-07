#백준 11286

import heapq as hq
import sys

input = sys.stdin.readline #빠른 입출력
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq,(abs(x),x))


    else:
        print(hq.heappop(pq)[1] if pq else 0)
        # if pq:
        #     print(hq.heappop(pq))
        # else:
        #     print(0)


