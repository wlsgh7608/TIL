"""
https://www.acmicpc.net/problem/1260
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(G,visited,vertex):
    """
    dfs는 스택 자료구조(재귀) 이용
    """
    visited[vertex] = True
    print(vertex+1, end = " ")
    for p in G[vertex]:
        if not visited[p]:
            dfs(G,visited,p)

def bfs(G,visited,vertex):
    """
    bfs는 큐 자료구조 이용
    """
    Q = deque()
    Q.append(vertex)
    visited[vertex] = True
    while Q:
        current  = Q.popleft()
        print(current+1,end = " ")
        for p in G[current]:
            if not visited[p]:
                Q.append(p)
                visited[p] = True

N, M, V = map(int,input().split())
G = [[]for _ in range(N)]
# 인접 리스트 생성
for _ in range(M):
    s,e = map(int,input().split())
    G[s-1].append(e-1)
    G[e-1].append(s-1)
for row in G:
    row.sort()
visited = [False for _ in range(N)]
dfs(G,visited,V-1)
print()
visited = [False for _ in range(N)]
bfs(G,visited,V-1) 



