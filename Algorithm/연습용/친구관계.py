import sys

n, m = map(int, input().split())
visited = [False] * n
graph = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs







