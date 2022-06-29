"""
토마토
https://www.acmicpc.net/problem/7576
15:56 ~ 16:25
bfs 사용(익은 토마토 일 수 체크하기 위함)
익은 토마토에 대하여 큐에 추가
만약 익지 않은 토마토(G = 0)가 있다면 -1 출력
익은 토마토들만 있다면 G값중 가장 큰 값-1 출력
"""
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().split())))
Q = deque()
# 처음 익은 토마토는 큐에 추가
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            Q.append((i,j))
mx_list = [-1,1,0,0]
my_list = [0,0,1,-1]
while Q:
    x,y = Q.popleft()
    
    for mx,my in zip(mx_list,my_list):
        nx = x + mx
        ny = y + my
        if 0<=nx <N and 0<=ny<M and G[nx][ny]== 0  : # 익지 않았다면
            Q.append((nx,ny))
            G[nx][ny] = G[x][y]+1 # days +1
            
max_days = 0
is_zero = False

# 익지 않은 토마토가 있는 지 , 최대 일 수 확인
for i in range(N):
    for j in range(M):
        if  G[i][j] == 0:
            is_zero = True
        max_days = max(max_days,G[i][j])
if is_zero:
    print(-1)
else:
    print(max_days-1)





