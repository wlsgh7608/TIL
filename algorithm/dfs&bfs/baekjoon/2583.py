"""
https://www.acmicpc.net/problem/2583
영역 구하기 / 실버 1 / 52분
실패 1(틀렸습니다)
 - 출력값을 제대로 보지 않음
22:30 ~ 23:22
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M,N,K = map(int,input().split())
points = []
X = [-1,1,0,0]
Y = [0,0,-1,1]



for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    points.append((y1,x1,y2,x2))

G = [[0 for _ in range(N)] for _ in range(M)]
for point in points:
    x1,y1,x2,y2 = point
    for i in range(x1,x2):
        for j in range(y1,y2):
            G[i][j] = 2

def dfs(x,y):
    G[x][y] = 1
    cnt=1
    for dx,dy in zip(X,Y):
        nx,ny = x+dx,y+dy
        if 0<=nx<M and 0<=ny<N:
            if G[nx][ny] == 0:
                cnt += dfs(nx,ny)
    return cnt


results = []
for i in range(M):
    for j in range(N):
        if G[i][j] == 0:
            result = dfs(i,j)
            results.append(result)
results.sort()
print(len(results))
print(*results)

"""
100 100 1
0 0 1 1

"""