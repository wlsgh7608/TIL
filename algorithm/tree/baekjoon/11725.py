"""
https://www.acmicpc.net/problem/11725
트리의 부모 찾기 / 실버 2 / 21분
17:06 ~ 17:27
"""
import sys
input = sys.stdin.readline

n = int(input())
G = [[] for _ in range(n)]

def bfs(n):
    from collections import deque
    Q = deque()
    Q.append(0)
    parent = [-1 for _ in range(n)]
    parent[0] = 0
    while Q:
        current = Q.popleft()
        for next in G[current]:
            if parent[next] == -1:
                parent[next] = current
                Q.append(next)
    return parent




for _ in range(n-1):
    a,b = map(int,input().split())
    a,b= a-1,b-1
    G[a].append(b)
    G[b].append(a)

parent = bfs(n)
for p in parent[1:]:
    print(p+1)





