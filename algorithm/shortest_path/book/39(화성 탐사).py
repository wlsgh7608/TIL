"""
(0,0) -> (N-1,N-1)로 가는 최단 경로만 찾으면 됨
: 다익스트라 알고리즘


"""

import sys
INF = sys.maxsize
imput = sys.stdin.readline
import heapq
X = [-1,1,0,0]
Y = [0,0,-1,1]
def dijkstra(v):
    visited = [[False for _ in range(N)] for _ in range(N)]
    Q = []
    heapq.heappush(Q,(G[v][v],v,v))
    while Q:
        w,x,y = heapq.heappop(Q)
        visited[x][y] = True
        if x==y== N-1: # 도착
            print(w)
            break
        for dx,dy in zip(X,Y):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: 
                heapq.heappush(Q,(w+G[nx][ny],nx,ny)) # 경로 추가

T = int(input())
for _ in range(T):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    M = [INF for _ in range(N)]
    dijkstra(0)


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""