"""
https://www.acmicpc.net/problem/2606
1번 컴퓨터부터 바이러스 시작
해당 컴퓨터와 인접한 컴퓨터에 대하여 방문하지 않았으면 cnt+1, 방문 표시
bfs을 이용하여 풀이
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
E = int(input())
G = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(E):
    s,e = map(int,input().split())
    G[s-1].append(e-1)
    G[e-1].append(s-1)
Q = deque()
Q.append(0)
visited[0] = True
cnt = 0
while Q:
    current = Q.popleft()
    for next in G[current]:
        if not visited[next]:
            visited[next] = True
            cnt+=1
            Q.append(next)
print(cnt)