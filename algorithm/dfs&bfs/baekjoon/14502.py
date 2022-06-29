"""
https://www.acmicpc.net/problem/14502
연구소 / 골드 5 / 40분
실패 1(시간 초과 1)
"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]


can_wall = []
for i in range(N):
    for j in range(M):
        if G[i][j]==0:
            can_wall.append([i,j])

from copy import deepcopy
max_cnt = 0
def bfs(x,y,visited,new_G):
    from collections import deque
    X = [-1,1,0,0]
    Y = [0,0,-1,1]
    Q = deque()
    Q.append((x,y))
    visited[x][y] = True
    while Q:
        c_x,c_y = Q.popleft()
        # print(c_x,c_y)
        for dx,dy in zip(X,Y):
            nx,ny = c_x+dx,c_y+dy
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and new_G[nx][ny] ==0:
                    visited[nx][ny] = True
                    new_G[nx][ny] = 2
                    Q.append((nx,ny))

def answer():
    new_G = deepcopy(G)
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if new_G[i][j] == 2:
                bfs(i,j,visited,new_G)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_G[i][j] == 0:
                cnt+=1
    return cnt

from itertools import combinations



canwall = list(combinations(can_wall,3))
max_cnt = 0
for wall in canwall:
    for x,y in wall:
        G[x][y] = 1
    result = answer()
    max_cnt = max(max_cnt,result)
    for x,y in wall:
        G[x][y] = 0

print(max_cnt)



