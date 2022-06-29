"""
https://www.acmicpc.net/problem/2644
촌수계산 / 실버 2 / 7분
03:56 ~ 04:03
"""
import sys
input = sys.stdin.readline
n = int(input())
start,end = map(int,input().split())
start,end = start-1,end-1
E = int(input())
G = [[]for _ in range(n)]
for _ in range(E):
    s,e = map(int,input().split())
    s,e = s-1,e-1
    G[s].append(e)
    G[e].append(s)

visited = [False for _ in range(n)]
from collections import deque
Q = deque()
Q.append((start,0))
visited[start] = True
answer = -1
while Q:
    current,cnt = Q.popleft()
    if current == end:
        answer = cnt
        break

    for next in G[current]:
        if not visited[next]:
            visited[next] = True
            Q.append((next,cnt+1))
print(answer)