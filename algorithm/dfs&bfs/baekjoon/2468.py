"""
https://www.acmicpc.net/problem/2468
안전 영역 / 실버 1 / 35분
15:35 ~  16:13
실패 1(틀렸습니다 1)
"""
import sys
sys.setrecursionlimit(10**6)
input =  sys.stdin.readline
n = int(input())
G = [list(map(int,input().split())) for _ in range(n)]

max_h = 0
for i in range(n):
    for j in range(n):
        max_h = max(max_h,G[i][j])
# 탐색
def dfs(x,y,h):
    X = [-1,1,0,0]
    Y = [0,0,-1,1]
    visited[x][y] = True
    for dx,dy in zip(X,Y):
        nx,ny=  x+dx,y+dy
        if 0<=nx<n and 0<=ny< n:
            if G[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = 1 # 방문 처리
                dfs(nx,ny,h) 
    return
max_cnt = 0
for h in range(max_h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 방문하지 않고 높이고 h보다 높을 경우 dfs 실행
            if G[i][j]>h and not visited[i][j] :
                dfs(i,j,h)
                cnt+=1
    max_cnt = max(max_cnt,cnt) # 최대 섬의 개수와 비교
print(max_cnt)
