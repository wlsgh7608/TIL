"""
https://www.acmicpc.net/problem/1987
알파벳 / 골드 4 / 2시간
10:15 ~ 
"""
import sys
input = sys.stdin.readline

R,C = map(int,input().split())
G =[]
max_cnt = 1
for _ in range(R):
    G.append(list(input()))
routes= set()
routes.add(G[0][0])

X = [-1,1,0,0]
Y = [0,0,-1,1]

def dfs(x,y,cnt):
    global max_cnt
    max_cnt = max(max_cnt,cnt)

    for i in range(4):
        nx = x + X[i]
        ny = y + Y[i]
    # for dx,dy in zip(X,Y):
        # nx,ny = x+dx,y+dy
        if 0<=nx < R and 0<=ny< C and G[nx][ny] not in routes:
            routes.add(G[nx][ny])
            dfs(nx,ny,cnt+1)
            routes.remove(G[nx][ny])

dfs(0,0,1)
print(max_cnt)