"""
https://www.acmicpc.net/problem/3055
탈출 / 골드 5 / 26분 
04:14 ~ 04:40
"""
import sys
input = sys.stdin.readline
from collections import deque
R,C = map(int,input().split())
M = []
for _ in range(R):
    M.append(input().rstrip())

G = [[0 for _ in range(C)] for _ in range(R)]

waters = []
start = 0
end = 0
for i in range(R):
    for j in range(C):
        if M[i][j] == 'S':
            start = (i,j)
        elif M[i][j] =='D':
            end = (i,j)
            G[i][j] = -3
        elif M[i][j] == '*':
            G[i][j] = -2
            waters.append((i,j))
        elif M[i][j] == 'X':
            G[i][j] = -1

Q = deque()
for water in waters:
    Q.append((water,0,True))
Q.append((start,0,False))

X = [-1,1,0,0]
Y = [0,0,-1,1]

result = -1
while Q:
    (x,y),cnt,is_water = Q.popleft()
    if end == (x,y):
        result = cnt
        break

    for dx,dy in zip(X,Y):
        nx,ny = x+dx,y+dy
        if 0<=nx<R and 0<=ny<C:
            if is_water and G[nx][ny]==0 :
                G[nx][ny] = -2
                Q.append(((nx,ny),cnt+1,is_water))
            elif not is_water and (G[nx][ny] ==0 or G[nx][ny] ==-3):
                G[nx][ny] = cnt+1
                Q.append(((nx,ny),cnt+1,is_water))

if result == -1:
    print('KAKTUS')
else:
    print(result)
