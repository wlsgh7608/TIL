import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x,y):
    X = [0,0,-1,1,1,1,-1,-1]
    Y = [1,-1,0,0,1,-1,-1,1]
    for dx,dy in zip(X,Y):
        nx = x + dx
        ny = y + dy
        if 0<=nx<h and 0<=ny<w:
            if G[nx][ny] == 1:
                G[nx][ny] = 2
                dfs(nx,ny)

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    G = []
    for _ in range(h):
        m = list(map(int,input().split()))
        G.append(m)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if G[i][j]==1:
                G[i][j]=2
                cnt+=1
                dfs(i,j)
    print(cnt)
                

