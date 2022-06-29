"""
https://www.acmicpc.net/problem/2146
다리만들기 / 골드 3 / 80분
실패 2:(틀렸습니다 2)
"""
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]


X = [-1,1,0,0]
Y = [0,0,-1,1]

# 섬 번호 만들어주기 
def bfs(x,y,number):
    Q = deque()
    Q.append((x,y))
    G[x][y] = number
    while Q:
        c_x,c_y = Q.popleft()
        for dx,dy in zip(X,Y):
            nx,ny = c_x+dx,c_y+dy
            if 0<=nx<N and 0<=ny< N:
                if G[nx][ny]==1:
                    G[nx][ny] = number
                    Q.append((nx,ny))

# 가장 짧은 다리 놓기
def bfs_answer(Q):
    results = []
    while Q:
        x,y = Q.popleft()
        for dx,dy in zip(X,Y):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if G[nx][ny] == 0:
                    G[nx][ny] = G[x][y]
                    cnt_land[nx][ny] = cnt_land[x][y]+1
                    Q.append((nx,ny))
                elif G[nx][ny]!= 0 and G[x][y]!=G[nx][ny]:
                    ans = cnt_land[nx][ny]+cnt_land[x][y]
                    results.append(ans)
    return min(results)

# 섬 번호는 2부터 시작
island_n = 2
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            bfs(i,j,island_n)
            island_n+=1

cnt_land=[[0 for _ in range(N)] for _ in range(N)]


Q = deque()
for i in range(N):
    for j in range(N):
        if G[i][j] != 0:
            Q.append((i,j))

result = bfs_answer(Q)
print(result)

"""
0회 간척:

1 1 0 0 0 1
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 0
1회 간척:

1 1 1 0 2 2
1 1 0 0 0 2
1 0 0 0 0 0
3 0 0 0 0 0
3 3 0 0 0 0
3 0 0 0 0 0

2회 간척:


5
1 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 1
0 0 0 0 1

"""