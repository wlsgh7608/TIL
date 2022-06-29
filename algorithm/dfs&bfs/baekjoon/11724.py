"""
https://www.acmicpc.net/problem/11724


"""
from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G= [[] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    G[s-1].append(e-1)
    G[e-1].append(s-1)
visited = [False for _ in range(N)]

cnt = 0
for i in range(N):
    if not visited[i]:
        start = i
        cnt +=1
        Q = deque()
        Q.append(start)
        visited[start] = True
        while Q:
            current  = Q.popleft()

            for next in G[current]:
                if next and not visited[next]:
                    Q.append(next)
                    visited[next] = True

print(cnt)