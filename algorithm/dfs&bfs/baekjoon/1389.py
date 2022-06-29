"""
https://www.acmicpc.net/problem/1389
케빈 베이컨의 6단계 법칙 / 실버 1 / 9분
04:05 ~ 04:14
"""
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    s,e = s-1,e-1
    G[s].append(e)
    G[e].append(s)


results = []
for i in range(N):
    Q = deque()
    visited = [0 for _ in range(N)]
    Q.append((i,0))
    visited[i]  = True
    while Q:
        current,cnt = Q.popleft()
        for next in G[current]:
            if not visited[next]:
                visited[next] = cnt+1
                Q.append((next,cnt+1))
    result = sum(visited)-1
    results.append(result)
min_idx,min_value = 0 , sys.maxsize
for i,v in enumerate(results):
    if min_value > v:
        min_idx = i
        min_value = v
print(min_idx+1)