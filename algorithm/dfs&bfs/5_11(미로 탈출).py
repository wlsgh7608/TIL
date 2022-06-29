import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().rstrip())))
Q =  deque()
Q.append((0,0,1)) # x,y, cnt
dx_list = [-1,1,0,0]
dy_list = [0,0,1,-1]
while Q:
    x,y,c = Q.popleft()
    if x == N-1 and y == M-1 :
        print(c)
        break
    for dx,dy in zip(dx_list,dy_list):
        nx ,ny = x + dx, y + dy
        if 0<= nx <N and 0<= ny < M and G[nx][ny] == 1:
            G[nx][ny] = 0
            Q.append((nx,ny,c+1))
        

