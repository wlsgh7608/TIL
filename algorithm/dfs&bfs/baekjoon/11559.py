"""
https://www.acmicpc.net/problem/11559
Puyo Puyo / 골드 4 / 70분
실패 2(틀렸습니다 2 )
"""
import sys
from collections import deque
input = sys.stdin.readline

G = [list(input().rstrip()) for _ in range(12)]

X = [-1,1,0,0]
Y = [0,0,1,-1]

def same_check(i,j):
    Q = deque()
    sames = []
    Q.append((i,j,G[i][j]))
    visited[i][j] = True
    sames.append((i,j))
    while Q:
        x,y,color = Q.popleft()
        for dx,dy in zip(X,Y):
            nx,ny = x+dx,y+dy
            if 0<=nx<12 and 0<=ny<6:
                if G[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    Q.append((nx,ny,color))
                    sames.append((nx,ny))
    if len(sames)>=4:
        return sames
    return

ans = 0
while True:
    same_results = []
    visited  = [[False for _ in range(6)] for _ in range(12)]
 
    for i in range(12):
        for j in range(6):
            if G[i][j] !='.' and not visited[i][j]:
                result = same_check(i,j)
                if result:
                    same_results.extend(result)
    if not same_results:
        break
    else:
        ans+=1
        same_results.sort(key= lambda x: (x[0],x[1]))
        for same in same_results:
            x_idx,y_idx = same
            for p in range(x_idx,0,-1):
                G[p][y_idx] = G[p-1][y_idx] 
            G[0][y_idx] = '.'
        continue

print(ans)
