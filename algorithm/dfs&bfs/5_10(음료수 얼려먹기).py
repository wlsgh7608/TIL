def dfs(x,y):
    dx_list = [-1,1,0,0]
    dy_list = [0,0,1,-1]
    G[i][j] = 1

    for dx,dy in zip(dx_list,dy_list):
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<M and G[nx][ny] == 0:
            G[nx][ny] = 1
            dfs(nx,ny)


import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().rstrip())))
    
cnt = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 0:
            dfs(i,j)
            cnt+=1
print(cnt)
"""
input
4 5 
00110
00011
11111
00000


output
3
"""